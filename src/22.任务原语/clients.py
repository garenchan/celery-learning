from celery import chain, group, chord

from tasks import add, xsum, raise_error, on_chord_error


if __name__ == '__main__':
    ## chain primitive
    res = chain(add.s(2, 2), add.s(4), add.s(8))()
    print('Chain result: %s' % res.get())
    
    # shortcut of above
    res = (add.s(2, 2) | add.s(4) | add.s(8))()
    print('Chain shortcut: %s' % res.get())
    
    res = chain(add.si(2, 2), add.si(4, 5), add.si(8, 8))()
    print('Chain with independent task: %s' % res.get())           # 8 + 8
    print('Parent result: %s' % res.parent.get())                  # 4 + 5
    print('Parent of parent result: %s' % res.parent.parent.get()) # 2 + 2
    
    
    ## group primitive
    res = group(add.s(i, i) for i in range(10))()
    print('Group result: %s' % res.get())
    
    
    ## chord primitive
    res = chord((add.s(i, i) for i in range(10)), xsum.s())()
    # is equal to: group(add.s(i, i) for i in range(10)) | xsum.s()
    print('Chord result: %s' % res.get())
    
    res = chord([add.s(2, 2), raise_error.s(), add.s(4, 4)], xsum.s())()
    print(res.get(propagate=False))
    
    print('Map result: %s' % ~xsum.map([list(range(10)), list(range(100))]))
    print('Starmap result: %s' % ~add.starmap(zip(range(10), range(10))))
    print('Chunks result: %s' % ~add.chunks(zip(range(100), range(100)), 10))



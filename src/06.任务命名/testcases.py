from tasks import add, sub
from tasks import app

@app.task
def main_module_task():
    pass

if __name__ == '__main__':
    assert add.name == 'custom_name'
    
    # If we not set task name, it will be '<module name>.<function name>'
    assert sub.name == 'tasks.sub'
    
    # If task in main module, it mean cannot decide its module name.
    # And if it not set name, its name will be '<app main module name>.<function name>'
    assert main_module_task.name == '.'.join([app.main, 'main_module_task'])
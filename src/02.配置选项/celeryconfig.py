############################################General settings########################################
# A white-list of content-types/serializers to allow.
# If a message is received that’s not in this list then the message will be discarded with an error.
# By default any content type is enabled, including pickle and yaml, so make sure untrusted parties 
# don’t have access to your broker.
# Default: {'json'} (set, list, or tuple).
accept_content = ['json']

#################################Time and date settings#############################################
# If enabled dates and times in messages will be converted to use the UTC timezone.
# Default: Enabled
enable_utc = True
# Configure Celery to use a custom time zone. The timezone value can be any time zone supported by 
# the pytz library.
# Default: "UTC".
timezone = None


##########################################Task settings#############################################
# This setting can be used to rewrite any task attribute from the configuration. The setting can be 
# a dict, or a list of annotation objects that filter for tasks and return a map of attributes to change.
# Default: None.
task_annotations = None
# Default compression used for task messages. Can be gzip, bzip2 (if available), or any custom 
# compression schemes registered in the Kombu compression registry.
# Default: None
task_compression = None
# Set the default task message protocol version used to send tasks. Supports protocols: 1 and 2.
# Default: 2 (since 4.0).
task_protocol = 2
# A string identifying the default serialization method to use. Can be json (default), pickle, yaml,
# msgpack, or any custom serialization methods that have been registered with kombu.serialization.registry.
# Default: "json" (since 4.0, earlier: pickle).
task_serializer = 'json'
# Decides if publishing task messages will be retried in the case of connection loss or other connection errors.
# Default: Enabled.
task_publish_retry = True
task_publish_retry_policy = {'interval_step': 0.2, 'max_retries': 3, 'interval_start': 0, 'interval_max': 1}


######################################Task execution settings#######################################
# If this is True, all tasks will be executed locally by blocking until the task returns.
# That is, tasks will be executed locally instead of being sent to the queue.
# Default: Disabled.
task_always_eager = False
# If this is True, eagerly executed tasks (applied by task.apply(), or when the task_always_eager 
# setting is enabled), will propagate exceptions.
task_eager_propagates = False
# If enabled task results will include the workers stack when re-raising task errors.
# Default: Disabled.
task_remote_tracebacks = False
# Whether to store the task return values or not (tombstones).
# Default: Disabled.
task_ignore_result = False
# If set, the worker stores all task errors in the result store even if Task.ignore_result is on.
# Default: Disabled.
task_store_errors_even_if_ignored = False
# If True the task will report its status as ‘started’ when the task is executed by a worker. 
# The default value is False as the normal behavior is to not report that level of granularity. 
# Tasks are either pending, finished, or waiting to be retried. Having a ‘started’ state can be 
# useful for when there are long running tasks and there’s a need to report what task is currently running.
# Default: Disabled.
task_track_started = True
# Task hard time limit in seconds. The worker processing the task will be killed and replaced with 
# a new one when this is exceeded.
# Default: No time limit.
task_time_limit = None
# The SoftTimeLimitExceeded exception will be raised when this is exceeded. For example, the task 
# can catch this to clean up before the hard time limit comes
task_soft_time_limit = None
# Late ack means the task messages will be acknowledged after the task has been executed, not just 
# before (the default behavior).
# Default: Disabled.
task_acks_late = False
# Even if task_acks_late is enabled, the worker will acknowledge tasks when the worker process 
# executing them abruptly exits or is signaled (e.g., KILL/INT, etc).
# Setting this to true allows the message to be re-queued instead, so that the task will execute 
# again by the same worker, or another worker.
task_reject_on_worker_lost = None
# The global default rate limit for tasks.
# This value is used for tasks that doesn’t have a custom rate limit
# Default: No rate limit.
task_default_rate_limit = None


################################Task result backend settings########################################
# The backend used to store task results (tombstones). Can be one of the following:
# rpc/database/redis/cache/cassandra/elasticsearch/ironcache/couchbase/couchdb/filesystem/consul
# Default: No result backend enabled by default.
result_backend = 'amqp://agent:agent@172.18.231.134:5672'
# Result serialization format.
# Default: json since 4.0 (earlier: pickle).
result_serializer = 'json'
# Optional compression method used for task results. Supports the same options as the 
# task_serializer setting.
# Default: No compression.
result_compression = None
# Time (in seconds, or a timedelta object) for when after stored task tombstones will be deleted.
# Default: Expire after 1 day.
# A built-in periodic task will delete the results after this time (celery.backend_cleanup), 
# assuming that celery beat is enabled. The task runs daily at 4am.
# A value of None or 0 means results will never expire (depending on backend specifications).
result_expires = 24 * 60 * 60
# Enables client caching of results.
# Default: Disabled by default.
# This can be useful for the old deprecated ‘amqp’ backend where the result is unavailable as soon
# as one result instance consumes it.
# This is the total number of results to cache before older results are evicted. A value of 0 or 
# None means no limit, and a value of -1 will disable the cache.
result_cache_max = -1

result_exchange_type = 'direct'
result_exchange = 'celeryresults'


###############################Database backend settings############################################
""" Database URL Examples
    To use the database backend you have to configure the result_backend setting with a connection 
    URL and the db+ prefix:
        result_backend = 'db+scheme://user:password@host:port/dbname'
    Examples:
        # sqlite (filename)
        result_backend = 'db+sqlite:///results.sqlite'
        # mysql
        result_backend = 'db+mysql://scott:tiger@localhost/foo'
        # postgresql
        result_backend = 'db+postgresql://scott:tiger@localhost/mydatabase'
        # oracle
        result_backend = 'db+oracle://scott:tiger@127.0.0.1:1521/sidname'
"""
# To specify additional SQLAlchemy database engine options you can use the sqlalchmey_engine_options
# setting:
# Default: {} (empty mapping).
database_engine_options = None
# Short lived sessions are disabled by default. If enabled they can drastically reduce performance, 
# especially on systems processing lots of tasks. This option is useful on low-traffic workers that 
# experience errors as a result of cached database connections going stale through inactivity. For 
# example, intermittent errors like (OperationalError) (2006, ‘MySQL server has gone away’) can be
# fixed by enabling short lived sessions. This option only affects the database backend.
# Default: Disabled by default.
database_short_lived_sessions = False
# When SQLAlchemy is configured as the result backend, Celery automatically creates two tables to 
# store result meta-data for tasks. This setting allows you to customize the table names:
# use custom table names for the database result backend.
#         database_table_names = {
#           'task':  'myapp_taskmeta',  # default: celery_taskmeta
#           'group': 'myapp_groupmeta', # default: celery_tasksetmeta
#         }
database_table_names = None


####################################RPC backend settings############################################
# If set to True, result messages will be persistent. This means the messages won’t be lost after a
# broker restart.
# Default: Disabled by default (transient messages).
result_persistent = None


###################################Cache backend settings###########################################
""" The cache backend supports the pylibmc and python-memcached libraries. 
    The latter is used only if pylibmc isn’t installed.
    
    Using a single Memcached server:
        result_backend = 'cache+memcached://127.0.0.1:11211/'
    Using multiple Memcached servers:
        result_backend = '''
            cache+memcached://172.19.26.240:11211;172.19.26.242:11211/
        '''.strip()
    The “memory” backend stores the cache in memory only:
        result_backend = 'cache'
        cache_backend = 'memory'
"""
# You can set pylibmc options using the cache_backend_options setting:
#       cache_backend_options = {
#           'binary': True,
#           'behaviors': {'tcp_nodelay': True},
#       }
# Default: {} (empty mapping).
cache_backend_options = {}
# This setting is no longer used as it’s now possible to specify the cache backend directly in the 
# result_backend setting
cache_backend = None


################################Redis backend settings##############################################
""" The Redis backend requires the redis library.
    To install this package use pip:
        $ pip install celery[redis]
    This backend requires the result_backend setting to be set to a Redis URL:
        result_backend = 'redis://:password@host:port/db'
"""
redis_host = None
redis_port = None
redis_password = None
redis_db = None
# The Redis backend supports SSL. The valid values of this options are the same as broker_use_ssl.
# Default: Disabled.
redis_backend_use_ssl = False
# Maximum number of connections available in the Redis connection pool used for sending and 
# retrieving results.
# Default: No limit.
redis_max_connections = -1
# New in version 5.0.1
# Socket timeout for connections to Redis from the result backend in seconds (int/float)
# Default: None
redis_socket_connect_timeout = None
# Socket timeout for reading/writing operations to the Redis server in seconds (int/float), used by 
# the redis result backend.
# Default: 120.0 seconds.
redis_socket_timeout = 120.0


################################Cassandra backend settings##########################################
""" This Cassandra backend driver requires cassandra-driver.
    To install, use pip:
        $ pip install celery[cassandra]
"""
# List of host Cassandra servers. For example: 
#     cassandra_servers = ['localhost']
# Default: [] (empty list).
cassandra_servers = []
# Port to contact the Cassandra servers on.
# Default: 9042.
cassandra_port = 9042
# The key-space in which to store the results. For example:
#     cassandra_keyspace = 'tasks_keyspace'
# Default: None.
cassandra_keyspace = None
# The table (column family) in which to store the results. For example:
#     cassandra_table = 'tasks'
cassandra_table = None
# The read consistency used. Values can be ONE, TWO, THREE, QUORUM, ALL, LOCAL_QUORUM, EACH_QUORUM, 
# LOCAL_ONE.
# Default: None.
cassandra_read_consistency = None
# The write consistency used. Values can be ONE, TWO, THREE, QUORUM, ALL, LOCAL_QUORUM, EACH_QUORUM,
# LOCAL_ONE.
# Default: None.
cassandra_write_consistency = None
# Time-to-live for status entries. They will expire and be removed after that many seconds after 
# adding. A value of None (default) means they will never expire.
# Default: None.
cassandra_entry_ttl = None
# AuthProvider class within cassandra.auth module to use. Values can be PlainTextAuthProvider or 
# SaslAuthProvider.
# Default: None.
cassandra_auth_provider = None
# Named arguments to pass into the authentication provider. For example:
#     cassandra_auth_kwargs  = {
#         username: 'cassandra',
#         password: 'cassandra'
#     }
cassandra_auth_kwargs = {}


#############################Elasticsearch backend settings#########################################
""" To use Elasticsearch as the result backend you simply need to configure the result_backend 
    setting with the correct URL.
    Example configuration
        result_backend = 'elasticsearch://example.com:9200/index_name/doc_type'
"""
# Should timeout trigger a retry on different node?
# Default: False
elasticsearch_retry_on_timeout = False
# Maximum number of retries before an exception is propagated.
# Default: 3.
elasticsearch_max_retries = 3
# Global timeout,used by the elasticsearch result backend.
# Default: 10.0 seconds.
elasticsearch_timeout = 10.0


######################################Riak backend settings#########################################
""" The Riak backend requires the riak library.
    To install the this package use pip:
        $ pip install celery[riak]
    This backend requires the result_backend setting to be set to a Riak URL:
        result_backend = 'riak://host:port/bucket'
"""
# This is a dict supporting the following keys: 
#   host: The host name of the Riak server. Defaults to "localhost".
#   port: The port the Riak server is listening to. Defaults to 8087.
#   bucket: The bucket name to connect to. Defaults to “celery”.
#   protocol: The protocol to use to connect to the Riak server. This isn’t configurable via result_backend
riak_backend_settings = {}


#################################AWS DynamoDB backend settings######################################
""" The Dynamodb backend requires the boto3 library.
    To install this package use pip:
        $ pip install celery[dynamodb]
    This backend requires the result_backend setting to be set to a DynamoDB URL:
        result_backend = 'dynamodb://aws_access_key_id:aws_secret_access_key@region:port/table?read=n&write=m'
"""


####################################IronCache backend settings######################################
""" The IronCache backend requires the iron_celery library:
    To install this package use pip:
        $ pip install iron_celery
    IronCache is configured via the URL provided in result_backend, for example:
        result_backend = 'ironcache://project_id:token@'
    Or to change the cache name:
        ironcache:://project_id:token@/awesomecache
"""


###################################Couchbase backend settings#######################################
""" The Couchbase backend requires the couchbase library.
    To install this package use pip:
        $ pip install celery[couchbase]
    This backend can be configured via the result_backend set to a Couchbase URL:
        result_backend = 'couchbase://username:password@host:port/bucket'
"""
# This is a dict supporting the following keys:
#     host: Host name of the Couchbase server. Defaults to localhost.
#     port: The port the Couchbase server is listening to. Defaults to 8091.
#     bucket: The default bucket the Couchbase server is writing to. Defaults to default.
#     username: User name to authenticate to the Couchbase server as (optional).
#     password: Password to authenticate to the Couchbase server (optional).
# Default: {} (empty mapping).
couchbase_backend_settings = {}


####################################CouchDB backend settings########################################
""" The CouchDB backend requires the pycouchdb library:
    To install this Couchbase package use pip:
        $ pip install celery[couchdb]
    This backend can be configured via the result_backend set to a CouchDB URL:
        result_backend = 'couchdb://username:password@host:port/container'
"""


####################################File-system backend settings####################################
""" This backend can be configured using a file URL, for example:
        result_backend = 'file:///var/celery/results'
    The configured directory needs to be shared and writable by all servers using the backend.
    If you’re trying Celery on a single system you can simply use the backend without any further 
    configuration. For larger clusters you could use NFS, GlusterFS, CIFS, HDFS (using FUSE), or 
    any other file-system.
"""


#################################Consul K/V store backend settings##################################
""" The Consul backend can be configured using a URL, for example:
        result_backend = ‘consul://localhost:8500/’
    The backend will storage results in the K/V store of Consul as individual keys.
    The backend supports auto expire of results using TTLs in Consul.
"""


###########################################Message Routing##########################################
# Most users will not want to specify this setting and should rather use the automatic routing facilities.
# If you really want to configure advanced routing, this setting should be a list of kombu.Queue 
# objects the worker will consume from.
# Note that workers can be overridden this setting via the -Q option, or individual queues from this 
# list (by name) can be excluded using the -X option.
# The default is a queue/exchange/binding key of celery, with exchange type direct.
# Default: None (queue taken from default queue settings).
task_queues = None
# A list of routers, or a single router used to route tasks to queues. When deciding the final 
# destination of a task the routers are consulted in order.
# A router can be specified as either:
#      * A function with the signature (name, args, kwargs, options, task=None, **kwargs)
#      * A string providing the path to a router function.
#      * A dict containing router specification: Will be converted to a celery.routes.MapRoute instance.
#      * A list of (pattern, route) tuples: Will be converted to a celery.routes.MapRoute instance.
# Examples:
#       task_routes = {
#           'celery.ping': 'default',
#           'mytasks.add': 'cpu-bound',
#           'feed.tasks.*': 'feeds',                           # <-- glob pattern
#           re.compile(r'(image|video)\.tasks\..*'): 'media',  # <-- regex
#           'video.encode': {
#               'queue': 'video',
#               'exchange': 'media'
#               'routing_key': 'media.video.encode',
#           },
#       }
#       task_routes = ('myapp.tasks.route_task', {'celery.ping': 'default})
#
#       Where myapp.tasks.route_task could be:
#           def route_task(self, name, args, kwargs, options, task=None, **kw):
#               if task == 'celery.ping':
#                   return {'queue': 'default'}
task_routes = None
# brokers:  RabbitMQ
# This will set the default HA policy for a queue, and the value can either be a string (usually all):
# Default: None.
# Using ‘all’ will replicate the queue to all current nodes, Or you can give it a list of nodes 
# to replicate to:
#     task_queue_ha_policy = ['rabbit@host1', 'rabbit@host2']
task_queue_ha_policy = None
# brokers:  RabbitMQ
# Default: None.
task_queue_max_priority = None
# This option enables so that every worker has a dedicated queue, so that tasks can be routed to 
# specific workers. Default: Disabled.
worker_direct = False
# If enabled (default), any queues specified that aren’t defined in task_queues will be automatically 
# created. Default: Enabled.
task_create_missing_queues = True
# The name of the default queue used by .apply_async if the message has no route or no custom queue 
# has been specified. Default: "celery".
# This queue must be listed in task_queues. If task_queues isn’t specified then it’s automatically 
# created containing one queue entry, where this name is used as the name of that queue.
task_default_queue = 'celery'
# Name of the default exchange to use when no custom exchange is specified for a key in the task_queues 
# setting. Default: "celery".
task_default_exchange = 'celery'
# Default exchange type used when no custom exchange type is specified for a key in the task_queues 
# setting. Default: "direct".
task_default_exchange_type = 'direct'
# The default routing key used when no custom routing key is specified for a key in the task_queues 
# setting. Default: "celery".
task_default_routing_key = 'celery'
# Can be transient (messages not written to disk) or persistent (written to disk).
# Default: "persistent".
task_default_delivery_mode = 2


##########################################Broker Settings###########################################
# Default broker URL. This must be a URL in the form of:
#     transport://userid:password@hostname:port/virtual_host
# Default: "amqp://"
# Only the scheme part (transport://) is required, the rest is optional, and defaults to the specific 
# transports default values.
# The transport part is the broker implementation to use, and the default is amqp, (uses librabbitmq 
# if installed or falls back to pyamqp). There are also other choices available, including; redis://, 
# sqs://, and qpid://.
#
# The scheme can also be a fully qualified path to your own transport implementation:
#     broker_url = 'proj.transports.MyTransport://localhost'
# More than one broker URL, of the same transport, can also be specified. The broker URLs can be 
# passed in as a single string that’s semicolon delimited:
#     broker_url = 'transport://userid:password@hostname:port//;transport://userid:password@hostname:port//'
# Or as a list:
#     broker_url = [
#           'transport://userid:password@localhost:port//',
#           'transport://userid:password@localhost:port//',
#     ]
# The brokers will then be used in the broker_failover_strategy.
broker_url = 'amqp://agent:agent@172.18.231.134:5672'
broker_password = None
broker_port = None
broker_transport = None
broker_user = None
broker_host = None
broker_vhost = None
# These settings can be configured, instead of broker_url to specify different connection parameters 
# for broker connections used for consuming and producing.
# Default: Taken from broker_url.
broker_read_url = 'amqp://agent:agent@172.18.231.134:5672'
broker_write_url = 'amqp://agent:agent@172.18.231.134:5672'
# Default failover strategy for the broker Connection object. If supplied, may map to a key in 
#‘kombu.connection.failover_strategies’, or be a reference to any method that yields a single item 
# from a supplied list.
# Example:
#     # Random failover strategy
#     def random_failover_strategy(servers):
#         it = list(servers) # don't modify callers list
#         shuffle = random.shuffle
#         for _ in repeat(None):
#             shuffle(it)
#             yield it[0]
#     broker_failover_strategy = random_failover_strategy
broker_failover_strategy = None
# transports supported:
#     pyamqp
# Note: This value is only used by the worker, clients do not use a heartbeat at the moment.
# Default: 120.0 (negotiated by server).
# It’s not always possible to detect connection loss in a timely manner using TCP/IP alone, so AMQP 
# defines something called heartbeats that’s is used both by the client and the broker to detect if 
# a connection was closed.
broker_heartbeat = 120
# transports supported:
#   pyamqp
# At intervals the worker will monitor that the broker hasn’t missed too many heartbeats. The rate 
# at which this is checked is calculated by dividing the broker_heartbeat value with this value, so 
# if the heartbeat is 10.0 and the rate is the default 2.0, the check will be performed every 5 
# seconds (twice the heartbeat sending rate).
broker_heartbeat_checkrate = 3.0
# transports supported:
#     pyamqp, redis
# Toggles SSL usage on broker connection and SSL settings.
# Default: Disabled.
# The valid values for this option vary by transport.
broker_use_ssl = False
# The maximum number of connections that can be open in the connection pool.
# The pool is enabled by default since version 2.5, with a default limit of ten connections. This 
# number can be tweaked depending on the number of threads/green-threads (eventlet/gevent) using a 
# connection. For example running eventlet with 1000 greenlets that use a connection to the broker, 
# contention can arise and you should consider increasing the limit.
# If set to None or 0 the connection pool will be disabled and connections will be established and 
# closed for every use.
broker_pool_limit = 10
# The default timeout in seconds before we give up establishing a connection to the AMQP server. 
# This setting is disabled when using gevent.
# Default: 4.0.
broker_connection_timeout = 4.0
# Automatically try to re-establish the connection to the AMQP broker if lost.
# The time between retries is increased for each retry, and is not exhausted before 
# broker_connection_max_retries is exceeded.
# Default: Enabled.
broker_connection_retry = True
# Maximum number of retries before we give up re-establishing a connection to the AMQP broker.
# Default: 100.
# If this is set to 0 or None, we’ll retry forever.
broker_connection_max_retries = 100
# Set custom amqp login method.
# Default: "AMQPLAIN".
broker_login_method = None
# A dict of additional options passed to the underlying transport.
# See your transport user manual for supported options (if any).
# Example setting the visibility timeout (supported by Redis and SQS transports):
#     broker_transport_options = {'visibility_timeout': 18000}  # 5 hours
# Default: {} (empty mapping).
broker_transport_options = {}


###########################################Worker###################################################
# A sequence of modules to import when the worker starts.
# This is used to specify the task modules to import, but also to import signal handlers and additional 
# remote control commands, etc.
# The modules will be imported in the original order.
# Default: [] (empty list).
imports = ()
# Exact same semantics as imports, but can be used as a means to have different import categories.
# The modules in this setting are imported after the modules in imports.
include = ()
# The number of concurrent worker processes/threads/green threads executing tasks.
# Default: Number of CPU cores.
# If you’re doing mostly I/O you can have more processes, but if mostly CPU-bound, try to keep it 
# close to the number of CPUs on your machine. If not set, the number of CPUs/cores on the host will be used.
worker_concurrency = 0
# How many messages to prefetch at a time multiplied by the number of concurrent processes. The 
# default is 4 (four messages for each process). The default setting is usually a good choice, 
# however – if you have very long running tasks waiting in the queue and you have to start the 
# workers, note that the first worker to start will receive four times the number of messages 
# initially. Thus the tasks may not be fairly distributed to the workers.
# To disable prefetching, set worker_prefetch_multiplier to 1. Changing that setting to 0 will allow 
# the worker to keep consuming as many messages as it wants.
worker_prefetch_multiplier = 4
# In some cases a worker may be killed without proper cleanup, and the worker may have published a 
# result before terminating. This value specifies how long we wait for any missing results before 
# raising a WorkerLostError exception.
worker_lost_wait = 10.0
# Maximum number of tasks a pool worker process can execute before it’s replaced with a new one. 
# Default is no limit.
worker_max_tasks_per_child = None
# Maximum amount of resident memory, in kilobytes, that may be consumed by a worker before it will 
# be replaced by a new worker. If a single task causes a worker to exceed this limit, the task will 
# be completed, and the worker will be replaced afterwards.
# Example:
#     worker_max_memory_per_child = 12000  # 12MB
worker_max_memory_per_child = None
# Disable all rate limits, even if tasks has explicit rate limits set.
# Default: Disabled (rate limits enabled).
worker_disable_rate_limits = False
# Name of the file used to stores persistent worker state (like revoked tasks). Can be a relative 
# or absolute path, but be aware that the suffix .db may be appended to the file name (depending on 
# Python version). Can also be set via the celery worker --statedb argument.
worker_state_db = None
# Set the maximum time in seconds that the ETA scheduler can sleep between rechecking the schedule.
# Setting this value to 1 second means the schedulers precision will be 1 second. If you need near 
# millisecond precision you can set this to 0.1.
worker_timer_precision = 1.0
# Specify if remote control of the workers is enabled.
# Default: Enabled by default.
worker_enable_remote_control = True


##############################################Events################################################
# Send task-related events so that tasks can be monitored using tools like flower. Sets the default 
# value for the workers -E argument.
# Default: Disabled by default.
worker_send_task_events = False
# If enabled, a task-sent event will be sent for every task so tasks can be tracked before they’re 
# consumed by a worker.
task_send_sent_event = False
# transports supported:
#     amqp
# Message expiry time in seconds (int/float) for when messages sent to a monitor clients event queue 
# is deleted (x-message-ttl). Default: 5.0 seconds.
# For example, if this value is set to 10 then a message delivered to this queue will be deleted after 10 seconds.
event_queue_ttl = 5.0
# transports supported:
#     amqp
# Expiry time in seconds (int/float) for when after a monitor clients event queue will be deleted (x-expires).
event_queue_expires = 60.0
# The prefix to use for event receiver queue names.
# Default: "celeryev".
event_queue_prefix = 'celeryev'
# Message serialization format used when sending event messages.
# Default: "json".
event_serializer = 'json'


####################################Remote Control Commands#########################################
# Time in seconds, before a message in a remote control command queue will expire.
# If using the default of 300 seconds, this means that if a remote control command is sent and no 
# worker picks it up within 300 seconds, the command is discarded.
# This setting also applies to remote control reply queues. Default: 300.0
control_queue_ttl = 300.0
# Time in seconds, before an unused remote control command queue is deleted from the broker.
# Default: 10.0. This setting also applies to remote control reply queues.
control_queue_expires = 10.0


############################################Logging#################################################
# By default any previously configured handlers on the root logger will be removed. If you want to 
# customize your own logging handlers, then you can disable this behavior by setting 
# worker_hijack_root_logger = False.
worker_hijack_root_logger = True
# Enables/disables colors in logging output by the Celery apps.
# Default: Enabled if app is logging to a terminal.
worker_log_color = None
# The format to use for log messages.
# Default:
#     "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"
worker_log_format = '[%(asctime)s: %(levelname)s/%(processName)s] %(message)s'
# The format to use for log messages logged in tasks.
# Default:
#     "[%(asctime)s: %(levelname)s/%(processName)s][%(task_name)s(%(task_id)s)] %(message)s"
worker_task_log_format = '[%(asctime)s: %(levelname)s/%(processName)s] %(task_name)s[%(task_id)s]: %(message)s'
# If enabled stdout and stderr will be redirected to the current logger.
# Default: Enabled by default. Used by celery worker and celery beat.
worker_redirect_stdouts = True
# The log level output to stdout and stderr is logged as. Can be one of DEBUG, INFO, WARNING, ERROR, or CRITICAL.
# Default: WARNING.
worker_redirect_stdouts_level = 'WARNING'


###########################################Security#################################################
# The relative or absolute path to a file containing the private key used to sign messages when 
# Message Signing is used. Default: None.
security_key = None
# The relative or absolute path to an X.509 certificate file used to sign messages when Message 
# Signing is used. Default: None.
security_certificate = None
# The directory containing X.509 certificates used for Message Signing. Can be a glob with wild-cards, 
# (for example /etc/certs/*.pem). Default: None.
security_cert_store = None


###########################Custom Component Classes (advanced)######################################
# Name of the pool class used by the worker.
# Default: "prefork" (celery.concurrency.prefork:TaskPool).
#
# Eventlet/Gevent
#     Never use this option to select the eventlet or gevent pool. You must use the -P option to celery 
#     worker instead, to ensure the monkey patches aren’t applied too late, causing things to break in strange ways.
worker_pool = 'prefork'
# If enabled the worker pool can be restarted using the pool_restart remote control command.
# Default: Disabled by default.
worker_pool_restarts = False
# Name of the autoscaler class to use.
# Default: "celery.worker.autoscale:Autoscaler".
worker_autoscaler = 'celery.worker.autoscale:Autoscaler'
# Name of the consumer class used by the worker.
# Default: "celery.worker.consumer:Consumer".
worker_consumer = 'celery.worker.consumer:Consumer'
# Name of the ETA scheduler class used by the worker. Default is or set by the pool implementation.
# Default: "kombu.async.hub.timer:Timer".
worker_timer = None

worker_pool_putlocks = True
worker_agent = None


#################################Beat Settings (celery beat)########################################
# The periodic task schedule used by beat.
# Default: {} (empty mapping).
beat_schedule = {}
# The default scheduler class. May be set to "django_celery_beat.schedulers:DatabaseScheduler" for 
# instance, if used alongside django-celery-beat extension.
# Default: "celery.beat:PersistentScheduler".
beat_scheduler = 'celery.beat:PersistentScheduler'
# Name of the file used by PersistentScheduler to store the last run times of periodic tasks. Can be 
# a relative or absolute path, but be aware that the suffix .db may be appended to the file name 
# (depending on Python version). Default: "celerybeat-schedule".
beat_schedule_filename = 'celerybeat-schedule'
# The number of periodic tasks that can be called before another database sync is issued. A value of
# 0 (default) means sync based on timing - default of 3 minutes as determined by scheduler.sync_every. 
# If set to 1, beat will call sync after every task message sent.
# Default: 0.
beat_sync_every = 0
# The maximum number of seconds beat can sleep between checking the schedule.
# Default: 0.
# The default for this value is scheduler specific. For the default Celery beat scheduler the value 
# is 300 (5 minutes), but for the django-celery-beat database scheduler it’s 5 seconds because the 
# schedule may be changed externally, and so it must take changes to the schedule into account.
beat_max_loop_interval = 0


############################################Other###################################################
mongodb_backend_settings = None
database_url = None
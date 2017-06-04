python graylog api client code

===


*  updateUser
   *  path : /users/{username}
   *  notes : 
   *  method : PUT
   *  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u'The name of the user to modify.'}, {u'paramType': u'body', u'required': True, u'type': u'ChangeUserRequest', u'name': u'JSON body', u'description': u'Updated user information.'}]
   *  summary : Modify user details.

*  removeStreamRule
  >*  path : /streams/{streamid}/rules/{streamRuleId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The stream id this new rule belongs to.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamRuleId', u'description': u''}]
  >*  summary : Delete a stream rule

*  createUserToken
  >*  path : /users/{username}/tokens/{name}
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'name', u'description': u'Descriptive name for this token (e.g. "cronjob") '}]
  >*  summary : Generates a new access token for a user

*  getUsers
  >*  path : /users
  >*  notes : The permissions assigned to the users are always included.
  >*  method : GET
  >*  parameters : []
  >*  summary : List all users

*  getAlarmCallback
  >*  path : /streams/{streamid}/alarmcallbacks/{alarmCallbackId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose alarm callbacks we want.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'alarmCallbackId', u'description': u'The alarm callback id we are getting'}]
  >*  summary : Get a single specified alarm callback for this stream

*  getSystemCollectors
  >*  path : /system/collectors
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Lists all existing collector registrations

*  createDebugEventsLocal
  >*  path : /system/debug/events/local
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': False, u'type': u'String', u'name': u'text', u'description': u''}]
  >*  summary : Create and send a local debug event

*  getIndicesReopened
  >*  path : /system/indexer/indices/reopened
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a list of reopened indices, which will not be cleaned by retention cleaning

*  getAlertConditions
  >*  path : /streams/{streamId}/alerts/conditions
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The stream id this new alert condition belongs to.'}]
  >*  summary : Get all alert conditions of this stream

*  createSearchSaved
  >*  path : /search/saved
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'CreateSavedSearchRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Create a new saved search

*  updateDashboard
  >*  path : /dashboards/{dashboardId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'UpdateDashboardRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update the settings of a dashboard.

*  removeUser
  >*  path : /users/{username}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u'The name of the user to delete.'}]
  >*  summary : Removes a user account.

*  updateBlacklistFilter
  >*  path : /filters/blacklist/{filterId}
  >*  notes : It can take up to a second until the change is applied
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'filterId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'FilterDescription', u'name': u'filterEntry', u'description': u''}]
  >*  summary : Update an existing blacklist filter

*  searchAbsolute
  >*  path : /search/universal/absolute
  >*  notes : Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'from', u'description': u'Timerange start. See description for date format'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'to', u'description': u'Timerange end. See description for date format'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'limit', u'description': u'Maximum number of messages to return.'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'offset', u'description': u'Offset'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'fields', u'description': u'Comma separated list of fields to return'}]
  >*  summary : Message search with absolute timerange.

*  getBundles
  >*  path : /system/bundles
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : List available content packs

*  updateGrok
  >*  path : /system/grok/{patternId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'patternId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'GrokPatternSummary', u'name': u'pattern', u'description': u''}]
  >*  summary : Update an existing pattern

*  getGrok
  >*  path : /system/grok/{patternId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'patternId', u'description': u''}]
  >*  summary : Get the existing grok pattern

*  searchKeyword
  >*  path : /search/universal/keyword
  >*  notes : Search for messages in a timerange defined by a keyword like "yesterday" or "2 weeks ago to wednesday".
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'keyword', u'description': u'Range keyword'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'limit', u'description': u'Maximum number of messages to return.'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'offset', u'description': u'Offset'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'fields', u'description': u'Comma separated list of fields to return'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'sort', u'description': u'Sorting (field:asc / field:desc)'}]
  >*  summary : Message search with keyword as timerange.

*  searchKeywordHistogram
  >*  path : /search/universal/keyword/histogram
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'interval', u'description': u'Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'keyword', u'description': u'Range keyword'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Datetime histogram of a query using keyword timerange.

*  removeDashboard
  >*  path : /dashboards/{dashboardId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}]
  >*  summary : Delete a dashboard and all its widgets

*  createSession
  >*  path : /system/sessions
  >*  notes : This request creates a new session for a user or reactivates an existing session: the equivalent of logging in.
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'SessionCreateRequest', u'name': u'Login request', u'description': u'Username and credentials'}]
  >*  summary : Create a new session

*  removeSearchSaved
  >*  path : /search/saved/{searchId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'searchId', u'description': u''}]
  >*  summary : Delete a saved search

*  getPermissionsReader
  >*  path : /system/permissions/reader/{username}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u''}]
  >*  summary : Get the initial permissions assigned to a reader account

*  applyBundle
  >*  path : /system/bundles/{bundleId}/apply
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'bundleId', u'description': u'Content pack ID'}]
  >*  summary : Set up entities described by content pack

*  updateUserPreferences
  >*  path : /users/{username}/preferences
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u'The name of the user to modify.'}, {u'paramType': u'body', u'required': True, u'type': u'UpdateUserPreferences', u'name': u'JSON body', u'description': u'The map of preferences to assign to the user.'}]
  >*  summary : Update a user's preferences set.

*  getStreamOutput
  >*  path : /streams/{streamid}/outputs/{outputId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose outputs we want.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'outputId', u'description': u'The id of the output we want.'}]
  >*  summary : Get specific output of a stream

*  updateAlertCondition
  >*  path : /streams/{streamId}/alerts/conditions/{conditionId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The stream id the alert condition belongs to.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'conditionId', u'description': u'The alert condition id.'}, {u'paramType': u'body', u'required': True, u'type': u'CreateConditionRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Modify an alert condition

*  getDebugEventsCluster
  >*  path : /system/debug/events/cluster
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Show last received cluster debug event

*  setLoggersSubsystemsLevel
  >*  path : /system/loggers/subsystems/{subsystem}/level/{level}
  >*  notes : Provided level is falling back to DEBUG if it does not exist
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'subsystem', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'level', u'description': u''}]
  >*  summary : Set the loglevel of a whole subsystem

*  getFields
  >*  path : /system/fields
  >*  notes : This operation is comparably fast because it reads directly from the indexer mapping.
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'limit', u'description': u'Maximum number of fields to return. Set to 0 for all fields.'}]
  >*  summary : Get list of message fields that exist

*  testLDAPSettings
  >*  path : /system/ldap/test
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'LdapTestConfigRequest', u'name': u'Configuration to test', u'description': u''}]
  >*  summary : Test LDAP Configuration

*  createStreamRule
  >*  path : /streams/{streamid}/rules
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The stream id this new rule belongs to.'}, {u'paramType': u'body', u'required': True, u'type': u'CreateStreamRuleRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Create a stream rule

*  getSystemPlugins
  >*  path : /system/plugins
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : List all installed plugins on this node

*  createGroks
  >*  path : /system/grok
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'Array', u'name': u'patterns', u'description': u''}]
  >*  summary : Update an existing pattern

*  getUser
  >*  path : /users/{username}
  >*  notes : The user's permissions are only included if a user asks for his own account or for users with the necessary permissions to edit permissions.
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u'The username to return information for.'}]
  >*  summary : Get user details

*  getMetricsNamespace
  >*  path : /system/metrics/namespace/{namespace}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'namespace', u'description': u''}]
  >*  summary : Get all metrics of a namespace

*  removeStream
  >*  path : /streams/{streamId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u''}]
  >*  summary : Delete a stream

*  getStreamRule
  >*  path : /streams/{streamid}/rules/{streamRuleId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose stream rule we want.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamRuleId', u'description': u'The stream rule id we are getting'}]
  >*  summary : Get a single stream rules

*  getBundle
  >*  path : /system/bundles/{bundleId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'bundleId', u'description': u'Content pack ID'}]
  >*  summary : Show content pack

*  getNode
  >*  path : /system/cluster/nodes/{nodeId}
  >*  notes : This is returning information of a node in context to its state in the cluster. Use the system API of the node itself to get system information.
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'nodeId', u'description': u''}]
  >*  summary : Information about a node.

*  getClusterStats
  >*  path : /system/cluster/stats
  >*  notes : This resource returns information about the Graylog cluster.
  >*  method : GET
  >*  parameters : []
  >*  summary : Cluster status information.

*  getSearchSavedAll
  >*  path : /search/saved
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a list of all saved searches

*  getStatsJvm
  >*  path : /system/stats/jvm
  >*  notes : This resource returns information about the Java Virtual Machine of this node.
  >*  method : GET
  >*  parameters : []
  >*  summary : JVM information about this node.

*  updateInputExtractor
  >*  path : /system/inputs/{inputId}/extractors/{extractorId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'extractorId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'CreateExtractorRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update an extractor

*  getBlacklistFilter
  >*  path : /filters/blacklist/{filterId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'filterId', u'description': u''}]
  >*  summary : Get the existing blacklist filter

*  getUserTokens
  >*  path : /users/{username}/tokens
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u''}]
  >*  summary : Retrieves the list of access tokens for a user

*  createRadioInput
  >*  path : /system/radios/{radioId}/inputs
  >*  notes : Radio inputs register their own inputs here for persistence after they successfully launched it.
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'radioId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'RegisterInputRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Register input of a radio.

*  getMetrics
  >*  path : /system/metrics
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all metrics

*  removeRadioInput
  >*  path : /system/radios/{radioId}/inputs/{inputId}
  >*  notes : Radios unregister their inputs when they are stopped/terminated on the radio.
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'radioId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : Unregister input of a radio.

*  getSearchSaved
  >*  path : /search/saved/{searchId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'searchId', u'description': u''}]
  >*  summary : Get a single saved search

*  searchRelativeTermsStats
  >*  path : /search/universal/relative/termsstats
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'key_field', u'description': u'Message field of to return terms of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'value_field', u'description': u'Value field used for computation'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'order', u'description': u'What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'size', u'description': u'Maximum number of terms to return'}, {u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'range', u'description': u'Relative timeframe to search in. See search method description.'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Ordered field terms of a query computed on another field using a relative timerange.

*  updateInputExtractorOrder
  >*  path : /system/inputs/{inputId}/extractors/order
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u'Persist ID (!) of input.'}, {u'paramType': u'body', u'required': True, u'type': u'OrderExtractorsRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update extractor order of an input

*  createDashboard
  >*  path : /dashboards
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'CreateDashboardRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Create a dashboard

*  closeIndex
  >*  path : /system/indexer/indices/{index}/close
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': False, u'type': u'String', u'name': u'index', u'description': u''}]
  >*  summary : Close an index. This will also trigger an index ranges rebuild job.

*  searchKeywordTerms
  >*  path : /search/universal/keyword/terms
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Message field of to return terms of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'size', u'description': u'Maximum number of terms to return'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'keyword', u'description': u'Range keyword'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Most common field terms of a query using a keyword timerange.

*  removeAlertReceiver
  >*  path : /streams/{streamId}/alerts/receivers
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The stream id this new alert condition belongs to.'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'entity', u'description': u'Name/ID of user or email address to remove from alert receivers.'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'type', u'description': u'Type: users or emails'}]
  >*  summary : Remove an alert receiver

*  getInput
  >*  path : /system/inputs/{inputId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : Get information of a single input on this node

*  createBundle
  >*  path : /system/bundles
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'ConfigurationBundle', u'name': u'Request body', u'description': u'Content pack'}]
  >*  summary : Upload a content pack

*  removeStreamOutput
  >*  path : /streams/{streamid}/outputs/{outputId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose outputs we want.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'outputId', u'description': u'The id of the output that should be deleted'}]
  >*  summary : Delete output of a stream

*  getSystemMessages
  >*  path : /system/messages
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'page', u'description': u'Page'}]
  >*  summary : Get internal Graylog system messages

*  createStreamOutput
  >*  path : /streams/{streamid}/outputs
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose outputs we want.'}, {u'paramType': u'body', u'required': True, u'type': u'AddOutputRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Associate outputs with a stream

*  removeUserPermissions
  >*  path : /users/{username}/permissions
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u'The name of the user to modify.'}]
  >*  summary : Revoke all permissions for a user without deleting the account.

*  removeOutput
  >*  path : /system/outputs/{outputId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'outputId', u'description': u'The id of the output that should be deleted'}]
  >*  summary : Delete output

*  restartInput
  >*  path : /system/inputs/{inputId}/restart
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : Restart existing input on this node

*  getGroks
  >*  path : /system/grok
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all existing grok patterns

*  getIndicesClosed
  >*  path : /system/indexer/indices/closed
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a list of closed indices that can be reopened.

*  searchRelativeFieldHistogram
  >*  path : /search/universal/relative/fieldhistogram
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Field of whose values to get the histogram of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'interval', u'description': u'Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)'}, {u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'range', u'description': u'Relative timeframe to search in. See search method description.'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Field value histogram of a query using a relative timerange.

*  searchKeywordStats
  >*  path : /search/universal/keyword/stats
  >*  notes : Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Message field of numeric type to return statistics for'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'keyword', u'description': u'Range keyword'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Field statistics for a query using a keyword timerange.

*  getStreams
  >*  path : /streams
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a list of all streams

*  createDebugEventsCluster
  >*  path : /system/debug/events/cluster
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': False, u'type': u'String', u'name': u'text', u'description': u''}]
  >*  summary : Create and send a cluster debug event

*  getFailuresCount
  >*  path : /system/indexer/failures/count
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'since', u'description': u'ISO8601 date'}]
  >*  summary : Total count of failed index operations since the given date.

*  getJob
  >*  path : /system/jobs/{jobId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'jobId', u'description': u''}]
  >*  summary : Get information of a specific currently running job

*  getAlarmCallbacksAvailable
  >*  path : /streams/{streamid}/alarmcallbacks/available
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose alarm callbacks we want.'}]
  >*  summary : Get a list of all alarm callback types

*  searchAbsoluteTermsStats
  >*  path : /search/universal/absolute/termsstats
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'key_field', u'description': u'Message field of to return terms of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'value_field', u'description': u'Value field used for computation'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'order', u'description': u'What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'size', u'description': u'Maximum number of terms to return'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'from', u'description': u'Timerange start. See search method description for date format'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'to', u'description': u'Timerange end. See search method description for date format'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Ordered field terms of a query computed on another field using an absolute timerange.

*  getBuffersClasses
  >*  path : /system/buffers/classes
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get classnames of current buffer implementations.

*  removeInput
  >*  path : /system/inputs/{inputId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : Terminate input on this node

*  getSources
  >*  path : /sources
  >*  notes : Range: The parameter is in seconds relative to the current time. 86400 means "in the last day", 0 is special and means "across all indices"
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'range', u'description': u'Relative timeframe to search in. See method description.'}]
  >*  summary : Get a list of all sources (not more than 5000) that have messages in the current indices. The result is cached for 10 seconds.

*  getIndicesRanges
  >*  path : /system/indices/ranges
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a list of all index ranges

*  removeIndex
  >*  path : /system/indexer/indices/{index}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': False, u'type': u'String', u'name': u'index', u'description': u''}]
  >*  summary : Delete an index. This will also trigger an index ranges rebuild job.

*  getDeflectorConfig
  >*  path : /system/deflector/config
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get deflector configuration. Only available on master nodes

*  removeNotification
  >*  path : /system/notifications/{notificationType}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': False, u'type': u'String', u'name': u'notificationType', u'description': u''}]
  >*  summary : Delete a notification

*  getBlacklistFilters
  >*  path : /filters/blacklist
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all blacklist filters

*  getMetricsNames
  >*  path : /system/metrics/names
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all metrics keys/names

*  getLDAPSettings
  >*  path : /system/ldap/settings
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get the LDAP configuration if it is configured

*  updateStreamRule
  >*  path : /streams/{streamid}/rules/{streamRuleId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The stream id this rule belongs to.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamRuleId', u'description': u'The stream rule id we are updating'}, {u'paramType': u'body', u'required': True, u'type': u'CreateStreamRuleRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update a stream rule

*  searchAbsoluteStats
  >*  path : /search/universal/absolute/stats
  >*  notes : Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Message field of numeric type to return statistics for'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'from', u'description': u'Timerange start. See search method description for date format'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'to', u'description': u'Timerange end. See search method description for date format'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Field statistics for a query using an absolute timerange.

*  getOutputsAvailable
  >*  path : /system/outputs/available
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all available output modules

*  resumeSystemProcessing
  >*  path : /system/processing/resume
  >*  notes : 
  >*  method : PUT
  >*  parameters : []
  >*  summary : Resume message processing

*  getNotifications
  >*  path : /system/notifications
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all active notifications

*  getInputsType
  >*  path : /system/inputs/types/{inputType}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputType', u'description': u''}]
  >*  summary : Get information about a single input type

*  getStatsFs
  >*  path : /system/stats/fs
  >*  notes : This resource returns information about the filesystems of this node.
  >*  method : GET
  >*  parameters : []
  >*  summary : Filesystem information about this node.

*  createAlarmCallback
  >*  path : /streams/{streamid}/alarmcallbacks
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The stream id this new alarm callback belongs to.'}, {u'paramType': u'body', u'required': True, u'type': u'CreateAlarmCallbackRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Create an alarm callback

*  getDeflector
  >*  path : /system/deflector
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get current deflector status

*  updateDashboardWidgetCacheTime
  >*  path : /dashboards/{dashboardId}/widgets/{widgetId}/cachetime
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'widgetId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'UpdateWidgetRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update cache time of a widget

*  getLoggers
  >*  path : /system/loggers
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : List all loggers and their current levels

*  reopenIndex
  >*  path : /system/indexer/indices/{index}/reopen
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': False, u'type': u'String', u'name': u'index', u'description': u''}]
  >*  summary : Reopen a closed index. This will also trigger an index ranges rebuild job.

*  getNodes
  >*  path : /system/cluster/nodes
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'nodeId', u'description': u''}]
  >*  summary : List all active nodes in this cluster.

*  createInputExtractor
  >*  path : /system/inputs/{inputId}/extractors
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'CreateExtractorRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Add an extractor to an input

*  getStreamRules
  >*  path : /streams/{streamid}/rules
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose stream rule we want.'}]
  >*  summary : Get a list of all stream rules

*  updateAlarmCallback
  >*  path : /streams/{streamid}/alarmcallbacks/{alarmCallbackId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The stream id this alarm callback belongs to.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'alarmCallbackId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'Map', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update an alarm callback

*  getStatsNetwork
  >*  path : /system/stats/network
  >*  notes : This resource returns information about the networking system this node is running with.
  >*  method : GET
  >*  parameters : []
  >*  summary : Networking information about this node.

*  getDashboard
  >*  path : /dashboards/{dashboardId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}]
  >*  summary : Get a single dashboards and all configurations of its widgets.

*  launchInput
  >*  path : /system/inputs/{inputId}/launch
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : Launch existing input on this node

*  getServiceManager
  >*  path : /system/serviceManager
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : List current status of ServiceManager

*  updateSearchSaved
  >*  path : /search/saved/{searchId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'searchId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'CreateSavedSearchRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update a saved search

*  getStatsOs
  >*  path : /system/stats/os
  >*  notes : This resource returns information about the operating system this node is running on.
  >*  method : GET
  >*  parameters : []
  >*  summary : OS information about this node.

*  getPermissions
  >*  path : /system/permissions
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all available user permissions.

*  setLoggersLevel
  >*  path : /system/loggers/{loggerName}/level/{level}
  >*  notes : Provided level is falling back to DEBUG if it does not exist
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'loggerName', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'level', u'description': u''}]
  >*  summary : Set the loglevel of a single logger

*  removeAlarmCallback
  >*  path : /streams/{streamid}/alarmcallbacks/{alarmCallbackId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The stream id this alarm callback belongs to.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'alarmCallbackId', u'description': u''}]
  >*  summary : Delete an alarm callback

*  getMessage
  >*  path : /messages/{index}/{messageId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'index', u'description': u'The index this message is stored in.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'messageId', u'description': u''}]
  >*  summary : Get a single message.

*  getStream
  >*  path : /streams/{streamId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u''}]
  >*  summary : Get a single stream

*  removeLDAPSettings
  >*  path : /system/ldap/settings
  >*  notes : 
  >*  method : DELETE
  >*  parameters : []
  >*  summary : Remove the LDAP configuration

*  updateUserPermissions
  >*  path : /users/{username}/permissions
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u'The name of the user to modify.'}, {u'paramType': u'body', u'required': True, u'type': u'PermissionEditRequest', u'name': u'JSON body', u'description': u'The list of permissions to assign to the user.'}]
  >*  summary : Update a user's permission set.

*  createStream
  >*  path : /streams
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'CreateStreamRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Create a stream

*  createOutput
  >*  path : /system/outputs
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'CreateOutputRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Create an output

*  getMetricsMultiple
  >*  path : /system/metrics/multiple
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'MetricsReadRequest', u'name': u'Requested metrics', u'description': u''}]
  >*  summary : Get the values of multiple metrics at once

*  shutdownNode
  >*  path : /system/shutdown/shutdown
  >*  notes : Attempts to process all buffered and cached messages before exiting, shuts down inputs first to make sure that no new messages are accepted.
  >*  method : POST
  >*  parameters : []
  >*  summary : Shutdown this node gracefully.

*  updateDashboardWidgetDescription
  >*  path : /dashboards/{dashboardId}/widgets/{widgetId}/description
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'widgetId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'UpdateWidgetRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update description of a widget

*  updateUserPassword
  >*  path : /users/{username}/password
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u'The name of the user whose password to change.'}, {u'paramType': u'body', u'required': True, u'type': u'ChangePasswordRequest', u'name': u'JSON body', u'description': u'The old and new passwords.'}]
  >*  summary : Update the password for a user.

*  getDebugEventsLocal
  >*  path : /system/debug/events/local
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Show last received local debug event

*  createAlertReceiver
  >*  path : /streams/{streamId}/alerts/receivers
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The stream id this new alert condition belongs to.'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'entity', u'description': u'Name/ID of user or email address to add as alert receiver.'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'type', u'description': u'Type: users or emails'}]
  >*  summary : Add an alert receiver

*  exportBundles
  >*  path : /system/bundles/export
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'ExportBundle', u'name': u'exportBundle', u'description': u'Export content pack'}]
  >*  summary : Export entities as a content pack

*  getInputExtractors
  >*  path : /system/inputs/{inputId}/extractors
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : List all extractors of an input

*  getInputs
  >*  path : /system/inputs
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all inputs of this node

*  getCountTotal
  >*  path : /count/total
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Total number of messages in all your indices.

*  getDashboards
  >*  path : /dashboards
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a list of all dashboards and all configurations of their widgets.

*  getNodeThis
  >*  path : /system/cluster/node
  >*  notes : This is returning information of this node in context to its state in the cluster. Use the system API of the node itself to get system information.
  >*  method : GET
  >*  parameters : []
  >*  summary : Information about this node.

*  getAlerts
  >*  path : /streams/{streamId}/alerts
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The stream id this new alert condition belongs to.'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'since', u'description': u'Optional parameter to define a lower date boundary. (UNIX timestamp)'}]
  >*  summary : Get the 300 most recent alarms of this stream.

*  getAlertsCheck
  >*  path : /streams/{streamId}/alerts/check
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The ID of the stream to check.'}]
  >*  summary : Check for triggered alert conditions of this streams. Results cached for 30 seconds.

*  cloneStream
  >*  path : /streams/{streamId}/clone
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'CloneStreamRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Clone a stream

*  getStats
  >*  path : /system/stats
  >*  notes : This resource returns information about the system this node is running on.
  >*  method : GET
  >*  parameters : []
  >*  summary : System information about this node.

*  updateInput
  >*  path : /system/inputs/{inputId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'InputLaunchRequest', u'name': u'JSON body', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : Update input on this node

*  getLoggersSubsystems
  >*  path : /system/loggers/subsystems
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : List all logger subsystems and their current levels

*  getClusterName
  >*  path : /system/indexer/cluster/name
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get the cluster name

*  getClusterHealth
  >*  path : /system/indexer/cluster/health
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get cluster and shard health overview

*  rebuildIndicesRanges
  >*  path : /system/indices/ranges/rebuild
  >*  notes : This triggers a systemjob that scans every index and stores meta information about what indices contain messages in what timeranges. It atomically overwrites already existing meta information.
  >*  method : POST
  >*  parameters : []
  >*  summary : Rebuild/sync index range information.

*  analyzeMessage
  >*  path : /messages/{index}/analyze
  >*  notes : Returns what tokens/terms a message string (message or full_message) is split to.
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'index', u'description': u'The index the message containing the string is stored in.'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'string', u'description': u'The string to analyze.'}]
  >*  summary : Analyze a message string

*  getMetricsHistory
  >*  path : /system/metrics/{metricName}/history
  >*  notes : The maximum retention time is currently only 5 minutes.
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'metricName', u'description': u''}, {u'paramType': u'query', u'required': False, u'type': u'Long', u'name': u'after', u'description': u'Only values for after this UTC timestamp (1970 epoch)'}]
  >*  summary : Get history of a single metric

*  getStreamsEnabled
  >*  path : /streams/enabled
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a list of all enabled streams

*  updateOutput
  >*  path : /system/outputs/{outputId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'outputId', u'description': u'The id of the output that should be deleted'}, {u'paramType': u'body', u'required': True, u'type': u'Map', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update output

*  updateLDAPSettings
  >*  path : /system/ldap/settings
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'LdapSettingsRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update the LDAP configuration

*  testAlertSendDummy
  >*  path : /streams/{streamId}/alerts/sendDummyAlert
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The stream id this new alert condition belongs to.'}]
  >*  summary : Send a test mail for a given stream

*  getSystemCollector
  >*  path : /system/collectors/{collectorId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'collectorId', u'description': u''}]
  >*  summary : Returns at most one collector summary for the specified collector id

*  getRadios
  >*  path : /system/radios
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : List all active radios in this cluster.

*  getOutputs
  >*  path : /system/outputs
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a list of all outputs

*  changeCollector
  >*  path : /system/collectors/{collectorId}
  >*  notes : This is a stateless method which upserts a collector registration
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'collectorId', u'description': u'The collector id this collector is registering as.'}, {u'paramType': u'body', u'required': True, u'type': u'CollectorRegistrationRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Create/update an collector registration

*  getSystemFailures
  >*  path : /system/indexer/failures
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'limit', u'description': u'Limit'}, {u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'offset', u'description': u'Offset'}]
  >*  summary : Get a list of failed index operations.

*  getStreamAllThroughput
  >*  path : /stream/throughput
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Current throughput of all visible streams on this node in messages per second

*  getClusterStatsElasticsearch
  >*  path : /system/cluster/stats/elasticsearch
  >*  notes : This resource returns information about the Elasticsearch Cluster.
  >*  method : GET
  >*  parameters : []
  >*  summary : Elasticsearch information.

*  searchKeywordFieldHistogram
  >*  path : /search/universal/keyword/fieldhistogram
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Field of whose values to get the histogram of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'interval', u'description': u'Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'keyword', u'description': u'Range keyword'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Datetime histogram of a query using keyword timerange.

*  searchRelative
  >*  path : /search/universal/relative
  >*  notes : Search for messages in a relative timerange, specified as seconds from now. Example: 300 means search from 5 minutes ago to now.
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'range', u'description': u'Relative timeframe to search in. See method description.'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'limit', u'description': u'Maximum number of messages to return.'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'offset', u'description': u'Offset'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'fields', u'description': u'Comma separated list of fields to return'}]
  >*  summary : Message search with relative timerange.

*  pauseSystemProcessing
  >*  path : /system/processing/pause
  >*  notes : 
  >*  method : PUT
  >*  parameters : []
  >*  summary : Pauses message processing

*  getSystem
  >*  path : /system
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get system overview

*  updateDashboardPositions
  >*  path : /dashboards/{dashboardId}/positions
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'WidgetPositionsRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update/set the positions of dashboard widgets.

*  getJournal
  >*  path : /system/journal
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get current state of the journal on this node.

*  pauseStream
  >*  path : /streams/{streamId}/pause
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u''}]
  >*  summary : Pause a stream

*  createBlacklistFilter
  >*  path : /filters/blacklist
  >*  notes : It can take up to a second until the change is applied
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'FilterDescription', u'name': u'filterEntry', u'description': u''}]
  >*  summary : Create a blacklist filter

*  getJVM
  >*  path : /system/jvm
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get JVM information

*  searchAbsoluteHistogram
  >*  path : /search/universal/absolute/histogram
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'interval', u'description': u'Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'from', u'description': u'Timerange start. See search method description for date format'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'to', u'description': u'Timerange end. See search method description for date format'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Datetime histogram of a query using an absolute timerange.

*  getBuffers
  >*  path : /system/buffers
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get current utilization of buffers and caches of this node.

*  getOutput
  >*  path : /system/outputs/{outputId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'outputId', u'description': u'The id of the output we want.'}]
  >*  summary : Get specific output

*  getStatsProcess
  >*  path : /system/stats/process
  >*  notes : This resource returns information about the process this node is running as.
  >*  method : GET
  >*  parameters : []
  >*  summary : Process information about this node.

*  searchKeywordTermsStats
  >*  path : /search/universal/keyword/termsstats
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'key_field', u'description': u'Message field of to return terms of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'value_field', u'description': u'Value field used for computation'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'order', u'description': u'What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'size', u'description': u'Maximum number of terms to return'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'keyword', u'description': u'Keyword timeframe'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Ordered field terms of a query computed on another field using a keyword timerange.

*  resumeStream
  >*  path : /streams/{streamId}/resume
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u''}]
  >*  summary : Resume a stream

*  removeUserToken
  >*  path : /users/{username}/tokens/{token}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'username', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'access token', u'description': u''}]
  >*  summary : Removes a token for a user

*  getInputsTypes
  >*  path : /system/inputs/types
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get all available input types of this node

*  removeGrok
  >*  path : /system/grok/{patternId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : []
  >*  summary : Remove an existing pattern by id

*  updateStream
  >*  path : /streams/{streamId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'UpdateStreamRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update a stream

*  getAlarmCallbacks
  >*  path : /streams/{streamid}/alarmcallbacks
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose alarm callbacks we want.'}]
  >*  summary : Get a list of all alarm callbacks for this stream

*  createInput
  >*  path : /system/inputs
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'InputLaunchRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Launch input on this node

*  createJob
  >*  path : /system/jobs
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'TriggerRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Trigger new job

*  searchRelativeTerms
  >*  path : /search/universal/relative/terms
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Message field of to return terms of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'size', u'description': u'Maximum number of terms to return'}, {u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'range', u'description': u'Relative timeframe to search in. See search method description.'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Most common field terms of a query using a relative timerange.

*  getMetric
  >*  path : /system/metrics/{metricName}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'metricName', u'description': u''}]
  >*  summary : Get a single metric

*  getInputExtractor
  >*  path : /system/inputs/{inputId}/extractors/{extractorId}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'extractorId', u'description': u''}]
  >*  summary : Get information of a single extractor of an input

*  getThreadDump
  >*  path : /system/threaddump
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get a thread dump

*  removeInputExtractor
  >*  path : /system/inputs/{inputId}/extractors/{extractorId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'extractorId', u'description': u''}]
  >*  summary : Delete an extractor

*  getClusterStatsMongo
  >*  path : /system/cluster/stats/mongo
  >*  notes : This resource returns information about MongoDB.
  >*  method : GET
  >*  parameters : []
  >*  summary : MongoDB information.

*  getStreamThroughput
  >*  path : /streams/{streamId}/throughput
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u''}]
  >*  summary : Current throughput of this stream on this node in messages per second

*  nextDeflectorCycle
  >*  path : /system/deflector/cycle
  >*  notes : 
  >*  method : POST
  >*  parameters : []
  >*  summary : Cycle deflector to new/next index

*  searchRelativeStats
  >*  path : /search/universal/relative/stats
  >*  notes : Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Message field of numeric type to return statistics for'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'range', u'description': u'Relative timeframe to search in. See search method description.'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Field statistics for a query using a relative timerange.

*  updateDashboardWidget
  >*  path : /dashboards/{dashboardId}/widgets/{widgetId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'widgetId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'AddWidgetRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Update a widget

*  pingRadio
  >*  path : /system/radios/{radioId}/ping
  >*  notes : Every graylog2-radio node is regularly pinging to announce that it is active.
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'radioId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'PingRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Ping - Accepts pings of graylog2-radio nodes.

*  getJobs
  >*  path : /system/jobs
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : List currently running jobs

*  searchAbsoluteFieldHistogram
  >*  path : /search/universal/absolute/fieldhistogram
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Field of whose values to get the histogram of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'interval', u'description': u'Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'from', u'description': u'Timerange start. See search method description for date format'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'to', u'description': u'Timerange end. See search method description for date format'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Field value histogram of a query using an absolute timerange.

*  getThroughput
  >*  path : /system/throughput
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Current throughput of this node in messages per second

*  searchAbsoluteTerms
  >*  path : /search/universal/absolute/terms
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'field', u'description': u'Message field of to return terms of'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': False, u'type': u'Integer', u'name': u'size', u'description': u'Maximum number of terms to return'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'from', u'description': u'Timerange start. See search method description for date format'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'to', u'description': u'Timerange end. See search method description for date format'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Most common field terms of a query using an absolute timerange.

*  removeAlertCondition
  >*  path : /streams/{streamId}/alerts/conditions/{conditionId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The stream id this new alert condition belongs to.'}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'conditionId', u'description': u'The stream id this new alert condition belongs to.'}]
  >*  summary : Delete an alert condition

*  createUser
  >*  path : /users
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'CreateUserRequest', u'name': u'JSON body', u'description': u'Must contain username, full_name, email, password and a list of permissions.'}]
  >*  summary : Create a new user account.

*  getRadioInputs
  >*  path : /system/radios/{radioId}/inputs
  >*  notes : This is returning the configured persisted inputs of a radio node. This is *not* returning the actually running inputs on a radio node. Radio nodes use this resource to get their configured inputs on startup.
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'radioId', u'description': u''}]
  >*  summary : Persisted inputs of a radio.

*  getIndices
  >*  path : /system/indexer/indices/{index}
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': False, u'type': u'String', u'name': u'index', u'description': u''}]
  >*  summary : Get information of an index and its shards.

*  removeBlacklistFilter
  >*  path : /filters/blacklist/{filterId}
  >*  notes : It can take up to a second until the change is applied
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'filterId', u'description': u''}]
  >*  summary : Remove the existing blacklist filter

*  updateLoadBalancerStatusOverride
  >*  path : /system/lbstatus/override/{status}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': False, u'type': u'String', u'name': u'status', u'description': u''}]
  >*  summary : Override load balancer status of this graylog2-server node. Next lifecycle change will override it again to its default. Set to ALIVE or DEAD

*  removeBundle
  >*  path : /system/bundles/{bundleId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'bundleId', u'description': u'Content pack ID'}]
  >*  summary : Delete content pack

*  getRadio
  >*  path : /system/radios/{radioId}
  >*  notes : This is returning information of a radio in context to its state in the cluster. Use the system API of the node itself to get system information.
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'radioId', u'description': u''}]
  >*  summary : Information about a radio.

*  getDashboardWidgetValue
  >*  path : /dashboards/{dashboardId}/widgets/{widgetId}/value
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'widgetId', u'description': u''}]
  >*  summary : Get a single widget value.

*  searchRelativeHistogram
  >*  path : /search/universal/relative/histogram
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'query', u'description': u'Query (Lucene syntax)'}, {u'paramType': u'query', u'required': True, u'type': u'String', u'name': u'interval', u'description': u'Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)'}, {u'paramType': u'query', u'required': True, u'type': u'Integer', u'name': u'range', u'description': u'Relative timeframe to search in. See search method description.'}, {u'paramType': u'query', u'required': False, u'type': u'String', u'name': u'filter', u'description': u'Filter'}]
  >*  summary : Datetime histogram of a query using a relative timerange.

*  removeSession
  >*  path : /system/sessions/{sessionId}
  >*  notes : Destroys the session with the given ID: the equivalent of logging out.
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'sessionId', u'description': u''}]
  >*  summary : Terminate an existing session

*  createInputStaticField
  >*  path : /system/inputs/{inputId}/staticfields
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'CreateStaticFieldRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Add a static field to an input

*  createDashboardWidget
  >*  path : /dashboards/{dashboardId}/widgets
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'AddWidgetRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Add a widget to a dashboard

*  getStreamOutputs
  >*  path : /streams/{streamid}/outputs
  >*  notes : 
  >*  method : GET
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamid', u'description': u'The id of the stream whose outputs we want.'}]
  >*  summary : Associate outputs with a stream

*  testMatchStream
  >*  path : /streams/{streamId}/testMatch
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u''}, {u'paramType': u'body', u'required': True, u'type': u'Map', u'name': u'JSON body', u'description': u''}]
  >*  summary : Test matching of a stream against a supplied message

*  getLoadBalancerStatus
  >*  path : /system/lbstatus
  >*  notes : 
  >*  method : GET
  >*  parameters : []
  >*  summary : Get status of this graylog2-server node for load balancers. Returns either ALIVE with HTTP 200 or DEAD with HTTP 503

*  removeInputStaticField
  >*  path : /system/inputs/{inputId}/staticfields/{key}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'Key', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : Remove static field of an input

*  removeDashboardWidget
  >*  path : /dashboards/{dashboardId}/widgets/{widgetId}
  >*  notes : 
  >*  method : DELETE
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'dashboardId', u'description': u''}, {u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'widgetId', u'description': u''}]
  >*  summary : Delete a widget

*  createAlertCondition
  >*  path : /streams/{streamId}/alerts/conditions
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'streamId', u'description': u'The stream id this new alert condition belongs to.'}, {u'paramType': u'body', u'required': True, u'type': u'CreateConditionRequest', u'name': u'JSON body', u'description': u''}]
  >*  summary : Create an alert condition

*  createGrok
  >*  path : /system/grok
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'body', u'required': True, u'type': u'GrokPatternSummary', u'name': u'pattern', u'description': u''}]
  >*  summary : Add a new named pattern

*  stopInput
  >*  path : /system/inputs/{inputId}/stop
  >*  notes : 
  >*  method : POST
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'inputId', u'description': u''}]
  >*  summary : Stop existing input on this node

*  updateBundle
  >*  path : /system/bundles/{bundleId}
  >*  notes : 
  >*  method : PUT
  >*  parameters : [{u'paramType': u'path', u'required': True, u'type': u'String', u'name': u'bundleId', u'description': u'Content pack ID'}, {u'paramType': u'body', u'required': True, u'type': u'ConfigurationBundle', u'name': u'Request body', u'description': u'Content pack'}]
  >*  summary : Update content pack

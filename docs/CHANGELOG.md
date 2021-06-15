# Version History
## v0.0.3
|||
|---|---|
|Date|2021-06-15
|Kind|Bugfix / Feature
|Author|mschiess@akamai.com <br> adrocho@akamai.com
- introduced line breaker variable for output
- fixed a bug in the "poll" handling
- fixed a bug that caused Popen PIPE to hang in certain circumstances
- bumped Dockerfile to newer CLI versions
- introduced RAW output (send data to stdout)


## v0.0.2
|||
|---|---|
|Date|2021-06-10
|Kind|Bugfix
|Author|mschiess@akamai.com <br> adrocho@akamai.com
- fixed monitoring output bug in docker-compose
- fixed bug in Dockerfile that prevented development builds
- fixed a bug in EAA CLI handler

## v0.0.1 (Initial Commit)
|version|v0.0.1|
|---|---|
|Date|2021-06-09
|Kind|Initial Commit
|Author|mschiess@akamai.com <br> adrocho@akamai.com
- INPUT: EAA, ETP, MFA (based on CLI's)
- OUTPUT: HTTP, TCP, UDP
- Docker & docker-compose examples
- Error & Reconnection handling
- Monitoring hook introduced Example:
- Kill Signal handling
- Configuration file `bin/config/global_config.py`
- Documentation & usage examples
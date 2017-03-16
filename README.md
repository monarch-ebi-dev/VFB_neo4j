VFB\_neo\_KB loading & update code:    [![Build Status](https://travis-ci.org/VirtualFlyBrain/VFB_neo4j.svg?branch=master)](https://travis-ci.org/VirtualFlyBrain/VFB_neo4j)


# VFB_neo4j

Neo4J servers:

* VFB\_neo_KB: The VFB knowledgeBase is the primary site of data-integration and annotations in VFB. It includes all of VFB's  annotation of images and the anatomy they depict. This database uses a standard schema to represent OWL, allowing us to use a generic transform to write OWL from the DB.  We are in the process of developing a standard pipeline to pull connectomic data into tthe KB from CATMAID.
  * STATUS: Transition from the older, MySQL representation of this data is almost complete.  Switchover should be complete by the end of 03/17.

* VFB\_neo_prod: production neo4J server.  This DB is built from a number of sources: OWL loaded via the OLS loader + some side loading from OWL via Jython scripts (These should be ditched if/when OLS supports importing the relevant axioms); Data directly imported from FlyBase; Data directly imported from VFB\_neo\_KB. 
  * STATUS:  In use. Imports from FlyBase are almost complete.

* VFB\_neo_dev: development version of the production server

Pipeline

![image](https://cloud.githubusercontent.com/assets/112839/23518012/fbf38b24-ff69-11e6-945a-378b1949ab81.png)

For details see [VFB pipeline doc](https://github.com/VirtualFlyBrain/VFB/blob/master/doc/pipeline.md)

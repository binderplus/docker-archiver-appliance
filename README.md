# Docker Archiver Appliance

This repository contains the [EPICS Archiver Appliance](https://slacmshankar.github.io/epicsarchiver_docs/) packaged to be easily run with `docker-compose`. The master branch currently uses [this release](https://github.com/slacmshankar/epicsarchiverap/releases/tag/v0.0.1_SNAPSHOT_13-Nov-2019).

## Getting started
Download and start the Archiver Appliance by running the following.
```bash
git clone https://github.com/binderplus/docker-archiver-appliance.git
cd docker-archiver-appliance
docker-compose up
```

You can then access the management console by going to http://localhost:17665/mgmt.

## Customization
You should edit the `.env` file to at least change the `MYSQL_PASSWORD` and `MYSQL_ROOT_PASSWORD`. The `ARCHAPPL_MYIDENTITY`, `EPICS_CA_ADDR_LIST` and `EPICS_CA_AUTO_ADDR_LIST` environment variables can also be set in that file.

The `appliances.xml` and `policies.py` files are located in `archappl/conf/` in case you need to modify those. 

The ports the Archiver Apppliance components listen to are determined by the entry in `appliances.xml` which corresponds to `ARCHAPPL_MYIDENTITY` (for example, if you don't change `appliances.xml` or `ARCHAPPL_MYIDENTITY` mgmt listens to port 17665).

The UI can be customized by placing images in `archappl/conf/site_specific_content/img` and creating the file `archappl/conf/site_specific_content/template_changes.html`. An example file `template_changes_sample.html` is provided. For more information consult the [documentation](https://slacmshankar.github.io/epicsarchiver_docs/site_specific_content_changes.html).

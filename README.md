# Docker Archiver Appliance

This repository contains the [EPICS Archiver Appliance](https://slacmshankar.github.io/epicsarchiver_docs/) packaged to be easily run with `docker-compose`.

## Getting started
Download and start the Archiver Appliance by running the following.
```bash
git clone https://github.com/binderplus/docker-archiver-appliance.git
cd docker-archiver-appliance
docker-compose up
```

You can then access the management console by going to http://localhost:17665/mgmt.

## Customization
You should edit the `environment` file to at least change the `MYSQL_PASSWORD` and `MYSQL_ROOT_PASSWORD`. The `ARCHAPPL_MYIDENTITY`, `EPICS_CA_ADDR_LIST` and `EPICS_CA_AUTO_ADDR_LIST` environment variables can also be set in that file.

The `appliances.xml` and `policies.py` files are located in `archappl/conf/`. The ports the Archiver Apppliance components listen to (for example, mgmt by default listens to port 17665) are determined by the entry in `appliances.xml` which corresponds to `ARCHAPPL_MYIDENTITY`.

The UI can be somewhat customized by placing images in `archappl/conf/site_specific_content/img` and creating the file `archappl/conf/site_specific_content/template_changes.html`. An example file `template_changes_sample.html` is provided. For more information consult the [documentation](https://slacmshankar.github.io/epicsarchiver_docs/site_specific_content_changes.html).
from datetime import time

import xmltodict
from panos.panorama import Panorama, PanoramaCommit, PanoramaCommitAll, Template
from panos.network import EthernetInterface

# create an object to represent our Panorama connection
pan = Panorama(PANURL, PANUSER, PANPASS)

# create an instance of our 'BaseTemplate' template within Panorama
template = Template("BaseTemplate")

# add our template instance to our Panorama object
pan.add(template)

# update the template object with data from our live Panorama instance
template.refresh()

# create an instance of our ethernet1/1 interface object
ifaces = EthernetInterface("ethernet1/1")

# add our interface instance to the template object
template.add(ifaces)

# update the interface object with data from the live Panorama instance
ifaces.refresh()

# take a look at what the interface is comprised of
ifaces.about()

# update the interface description
ifaces.comment = "WAN network"

# push our interface object to Panorama's candidate configuration
ifaces.apply()

# create a commit object with our description and admin user as a list
pan_commit = PanoramaCommit("pushed from pan-os-docker", ["automation"])

# pass our commit object into the commit method of our panorama instance
commit_job = pan.commit(cmd=pan_commit)

# create a object called 'job_complete' and set it to False for now
job_complete = False

# while the job_complete object is set to False (default), perform this task
while not job_complete:
    # check in on the status of our job, storing the XML byte response
    response = pan.op(cmd=f'show jobs id "{commit_job}"', xml=True)
    # convert the XML byte response object to a Python dictionary
    job_as_dict = xmltodict.parse(response)
    job = job_as_dict["response"]["result"]["job"]
    # check in on status of commit job, report back to screen
    if job["id"] == str(commit_job):
        if job["type"] == "Commit":
            if job["progress"] == "100":
                if job["status"] == "FIN":
                    if job["result"] == "OK":
                        print("[DEBUG] Job Finished, 100 Percent and Results are OK")
                        job_complete = True
                        break
                    else:
                        print(
                            "[DEBUG] Job Finished, 100 Percent and Results are not OK: %s "
                            % job["result"]
                        )
                else:
                    print(
                        "[DEBUG] Job progress is 100 Percent but status is not FIN: %s "
                        % job["status"]
                    )
            else:
                print(
                    "[DEBUG] Job progress is not 100 Percent yet ... %s "
                    % job["progress"]
                )
        else:
            print("[DEBUG] Job is not a COMMIT job : %s " % job["type"])
    if not job_complete:
        time.sleep(5)

    job = job_as_dict["result"]["job"]

# create an empty list and beging to iterate over our device groups
jobs = []
for dg in ["branch", "headquarters"]:
    # create a commit object, passing in the style and device group name
    dg_commit = PanoramaCommitAll("device group", dg)
    # send our commit operation to Panorama and store the job id
    job_id = pan.commit(cmd=dg_commit)
    # append our job id to the `jobs` list created above.
    jobs.append(job_id)

print(jobs)

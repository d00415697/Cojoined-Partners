Description
You will be deploying an app for 1-3 students that are currently in the SE3200 class.

Requirements
You will be added as a github collaborator on their repository. You will need to bundle the app in docker and then deploy via kubernetes. You should communicate via the discussion portal on the github repository. I will be looking for some communication. Likely you may need to ask a question or two and then inform them of the ip/hostname where the app is running.

All of your endpoints should be accessible over port 80. You will utilize an ingress controller to make this happen. (They will need to make sure that all their api requests in their javascript file go to the correct port).

The app will consist of a frontend and backend. They should scale independently of each other. The backend will be weird if you run a replica of more than one.

All of your files (docker, k8s) should be placed and committed to the git repo that is shared with you.

You should also augment the README file with the following information:

how to build the docker containers and push to docker hub
how to apply the kubernetes yaml files
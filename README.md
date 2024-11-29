# Streamlit with Google Cloud Run

This code is forked from [mktaop](https://github.com/mktaop/cloudrun_demo), demo'ing a simple Streamlit App that Google can run on Cloud Run. His step by step video is [located here](https://www.youtube.com/watch?v=BGMdxpXsbB4).

### Step by Steps

1. Select / Search for Cloud Run, and Deploy Container (as Service) ![](images/cloud-run.png)
2. Deploy from git, and ensure the username is connected (validating your Git account). You may need to install Cloud Build for the repositories ![](images/deploy-from-git.png). Once Cloud Build is enabled for Git, you should be able to view all of your repositories. For "Build Type", select Dockerfile.
3. Specify the service. ![](images/specify-service.png). For authentication, you can `Allow unauthenticated invocations` to enable this website to be accessed from the public. As well, you may wish to set CPUs to only be allocated per request (which means you're only charged when someone sends a request to your site).

### Requirements 

Please read for what's required in terms of roles and API!

You will need the following roles:

  -Cloud Build Service Account (roles/cloudbuild.builds.builder)
  
  -Cloud Run Admin (roles/run.admin)
  
  -Service Account User (roles/iam.serviceAccountUser)
  
Enable Billing for your project

Enable Cloud Build API & Cloud Run Admin API

Enable Identity and Access Management (IAM) API

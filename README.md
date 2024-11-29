# Streamlit with Google Cloud Run

This code is forked from [mktaop](https://github.com/mktaop/cloudrun_demo), demo'ing a simple Streamlit App that Google can run on Cloud Run. His step by step video is located here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/BGMdxpXsbB4?si=7gMigcuQUzgTn5lH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Original Steps

Please read for what's required in terms of roles and API!

You will need the following roles:

  -Cloud Build Service Account (roles/cloudbuild.builds.builder)
  
  -Cloud Run Admin (roles/run.admin)
  
  -Service Account User (roles/iam.serviceAccountUser)
  
Enable Billing for your project

Enable Cloud Build API & Cloud Run Admin API

Enable Identity and Access Management (IAM) API

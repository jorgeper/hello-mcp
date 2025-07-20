## Docker
1. Build docker image and push locally
   ```docker build -t hello-mcp .```

2. Tag it
   ```docker tag hello-mcp buzzzzacr.azurecr.io/hello-mcp```

3. Push to Azure ACR
   ```docker push buzzzzacr.azurecr.io/hello-mcp:latest```

4. List
   ```az acr repository list --name buzzzzacr --output table```

5. Deploy container, use Azure UX.
   Creates container instance `hello-mcp.gee0bchmhwa7hsaq.westus2.azurecontainer.io`
   Make sure to select port 8080
   TODO: python code hardcodes port 8080 look at how to not do this and pass through env of whatnot.
   `curl http://4.155.94.5:8080/tools`


## 7/19/25

1. Created hello world mcp server
2. Got it to run locally with cursor
3. Built a docker file, run it locally with docker
4. Deploying it in azure (tried railways app but didn't like it)

### Next
1. Deploy SSE since N8N doesn't seem to take HTTP
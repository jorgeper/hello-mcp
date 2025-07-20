## Docker
1. Build docker image and push locally
   ```docker buildx build --platform linux/amd64 -t hello-mcp .```

2. Tag it
   ```docker tag hello-mcp buzzzzacr.azurecr.io/hello-mcp```

3. Login to ACR
   ```az acr login --name buzzzzacr```

4. Push to Azure ACR
   ```docker push buzzzzacr.azurecr.io/hello-mcp:latest```

5. List
   ```az acr repository list --name buzzzzacr --output table```

6. Deploy container, use Azure UX.
   Creates container instance `hello-mcp.gee0bchmhwa7hsaq.westus2.azurecontainer.io`
   Make sure to select port 8080
   TODO: python code hardcodes port 8080 look at how to not do this and pass through env of whatnot.
   `curl http://4.155.94.5:8080/tools`

7. View logs
   ```az container logs --resource-group buzzzbuzz-rg --name hello-mcp```
   ```watch -n 2 "az container logs --resource-group buzzzzbuzz-rg --name hello-mcp-instance"```

## 7/19/25

1. Created hello world mcp server
2. Got it to run locally with cursor
3. Built a docker file, run it locally with docker
4. Deploying it in azure (tried railways app but didn't like it)

## 7/20/25

- Got it all to work. Claude was using the wrong mcp import.
- Now n8n can run my tool but it's getting an internal error.

### Next

- Figure out how to debug given correlation id. Somehow traces not showing up
- Clean the whole thing up.
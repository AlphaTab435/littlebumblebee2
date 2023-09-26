imageName="        image: muhammadtabish/bankist-app"

with open('version.txt', 'r') as file:
    Version=file.read()
    # print(Version)
with open('kustomize/deployment.yml', 'r') as file:
    deploymentContent = file.read()
    # print(deploymentContent)


splitDepoymentContent=deploymentContent.split("\n")
# print(splitDepoymentContent)

newDeployment=""
for str in splitDepoymentContent:
    if(imageName not in str):
        newDeployment+=str+"\n"
    else:
        print(imageName+Version+"  # Replace with your Docker image and tag\n")
        newDeployment+=imageName+":"+Version+"  # Replace with your Docker image and tag\n"
# print(newDeployment)

with open('kustomize/deployment.yml', 'w') as file:
    file.write(newDeployment)

# with open('output.yml', 'w') as file:
#     file.write(newDeployment)

# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

#### Virtual machine

A virtual machine gives more control because I can manage the operating system,
Python version, web server, network, and packages. But it also means more work.
I need to install updates, configure the server, monitor it, and make sure the
application starts correctly.

A small VM can have a simple monthly cost, but one VM can stop working and make
the website unavailable. For better availability, I would need more VMs and a
load balancer, so the cost and work will increase. Scaling also needs more
manual configuration because I need to resize the VM or create more VMs with
the same setup.

#### Azure App Service

Azure App Service manages the server and operating system for me. It also gives
the application an HTTPS address and can restart the application when needed.
The service plan has a cost, but it saves time because I do not need to manage a
complete server.

It is easier to scale App Service by changing the plan or adding more instances.
This can also improve availability. For the deployment workflow, I connected
the GitHub repository to App Service with GitHub Actions. When the workflow
runs, it builds the Python project and deploys it to Azure. The SQL, Blob
Storage, and Microsoft login values are saved in the App Service environment
variables and not in the source code.

#### Decision

I selected Azure App Service for this CMS application. The project is a Flask
application with Python 3.10 and it does not need special access to the operating
system. App Service works with Azure SQL Database, Blob Storage, Microsoft Entra
ID, logs, and GitHub Actions. For me, it was easier to configure and deploy than
a VM, and it will also be easier to scale later.

### Assess app changes that would change your decision.

I could change my decision if the application needs software that App Service
does not support, special drivers, more control of the operating system, or a
special network configuration. In these cases, a VM can be a better option
because I can control all the server configuration.

If the application only gets more users, I would first try to scale App Service
instead of moving to a VM. Azure SQL Database and Blob Storage already keep the
data outside the web application. I could use a bigger App Service plan, more
instances, health checks, and better monitoring. If the application becomes
much more complex and needs different background services, I could also
consider containers in the future.

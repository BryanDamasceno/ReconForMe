# ReconForMe

## Passive recon and information gathering automation.

This script automates the use of some tools for the reconnaissance phase in a pentest using a domain.

You must have installed on your machine:

```
- nmap: https://nmap.org/
- subfinder: https://github.com/projectdiscovery/subfinder
- nuclei: https://github.com/projectdiscovery/nuclei
```

To consult the shodan search engine (https://shodan.io) it is necessary to have an account on the platform and purchase an api key. Put the api key in an "api.txt" file at the root of the project.

You must add the CVEs templates in the "templates" folder, so that they can be used by nuclei during the target scan.

Run the program with the command:

```
python3 ReconForMe.py
```

After running the script the results can be found in the "report" folder that was created.

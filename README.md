# Test task for URSiP
Excel file parser made with Django framework.

## Requirements

To use this app you need for Docker and Docker Compose plugin to be installed.
You can find all the necessary on their website:

https://docs.docker.com/get-docker/

https://docs.docker.com/compose/install/

## How to install

**Step 1.** Clone the app from GitHub:
```
git clone git@github.com:feodorov1992/XLSX_parser.git
```
And move to the cloned app directory (where `docker-compose.yml` file is).

**Step 2.** Use docker-compose to build and start the app:
```
docker-compose up -d
```

## How to use
To access the app please open your localhost address in browser (default port).

Main links are located in the top of each page

### Home page

http://127.0.0.1

Home page contains standard file upload form. If the file you've provided is correct, you will be redirected to the result page

### File history page

http://127.0.0.1/files

File history page contains the list of all files you've uploaded (if any) and links to the parsing result.

### Parsing result page

>It is impossible to provide th direct address to suck pages beause they are auto-generated
>
>You can access them from File history page

These pages contain results of each uploaded file parsing result

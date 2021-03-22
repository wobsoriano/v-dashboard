# SRE Dashboard

SRE Dashboard is a dashboard for viewing, editing and analyzing Service Level
Objectives. It works in tandem with the `slo-generator` and requires the 
`Bigquery` exporter to be setup as it queries all data from BigQuery. 

SRE Dashboard is useful for both SRE teams and application teams to get a feel 
of where they're at in their SRE journey, SLO adoption and SLO targets.

## Backend
SRE Dashboard backend is written in Flask (Python). It is a simple interfacing 
layer to make queries to BigQuery.

### Setup
```
cp backend/.env.sample backend/.env
```
Set all the required environment variables in `backend/.env` file.

### Run backend
```
cd backend/
source .env
flask run
```

## Frontend
SRE Dashboard frontend is written in VueJS 3 for the UI framework, and Tailwind 
CSS for the HTML / CSS styling.

### Project setup
```
yarn
```

### Compiles and hot-reloads for development
```
yarn dev
```

### Compiles and minifies for production
```
yarn build
```

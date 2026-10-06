# Nginx serves the static files (lightweight Alpine version)
FROM nginx:alpine

COPY index.html script.js /usr/share/nginx/html/

EXPOSE 80

# No CMD needed the nginx image already starts the server
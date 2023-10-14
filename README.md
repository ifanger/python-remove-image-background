
### Install gunicorn
```pip3 install gunicorn```

### Run application with gunicorn
```gunicorn -w 4 server:app -b 127.0.0.1:8000```

*Note:* You must setup a Nginx server with a proxy configuration that redirects to your gunicorn port.

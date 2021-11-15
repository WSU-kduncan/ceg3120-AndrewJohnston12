# HAP Configuration & Documentation
You can install haproxy by typing in this in into
your terminal "sudo apt install haproxy"

The /etc/haproxy/haproxy.cfg file is the primary configuration file for haproxy and no other files were modified and the location is /etc/haproxy/haproxy.cfg 

default configurations were set with haproxy 

you dont need to restart the service after a new configuration you can use the 
reload function and it will do the same thing as reloading 

Sources:
https://www.haproxy.org/download/1.7/doc/management.txt
https://www.haproxy.com/blog/how-to-install-haproxy-on-ubuntu/
https://www.haproxy.com/blog/introduction-to-haproxy-maps/
https://cbonte.github.io/haproxy-dconv/2.4/configuration.html


# Server 1 & 2 Configuration & Documentation
You can install Apache webserver by typing in this in into
your terminal "sudo apt install apache2"

the file apache2.conf files was modifiled and no other files were modified and the location is /etc/apache2/apache.conf

default configurations were set with Apache

you can restart apache by typing the command "sudo service apache2 restart"

Source:
http://httpd.apache.org/docs/current/configuring.html
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
https://www.cyberciti.biz/faq/star-stop-restart-apache2-webserver/

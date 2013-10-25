ocpcatmaid
==========

Caching gateway to connect a CATMAID server to the Open Connectome Project Web Services


  ** setup **
  
  Using mysql we need to creat the following tables.  The must be reabable by django, i.e. configure with the same database user used in django. 

  create database ocpcatmaid;
  use ocpcatmaid
  CREATE TABLE contents ( url varchar(255), reftime TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (reftime, url)); 


  Make a directory for logging. It has to have permission for the Web server (www-data or your user for the development server)

    mkdir /var/log/ocpcatmaid


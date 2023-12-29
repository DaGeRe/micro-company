FROM eclipse-temurin:8
VOLUME /tmp
ADD monolithic-*.jar /app.jar
ADD kieker-1.15.4-aspectj.jar /kieker-1.15.4-aspectj.jar 
RUN bash -c 'touch /app.jar'
EXPOSE 8080
CMD ["java","-javaagent:kieker-1.15.4-aspectj.jar","-Dspring.profiles.active=docker","-jar","/app.jar"]

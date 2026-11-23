FROM eclipse-temurin:17-jre
COPY target/quote-api.jar /app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]

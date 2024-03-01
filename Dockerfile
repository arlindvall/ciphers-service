FROM eclipse-temurin:17
WORKDIR /home
COPY ./target/ciphers-service-0.0.1-SNAPSHOT.jar ciphers-service.jar
ENTRYPOINT ["java", "-jar", "ciphers-service.jar"]
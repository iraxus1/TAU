FROM maven:3-openjdk-17-slim AS MAVEN_BUILD
#copy the pom.xml file to the image
COPY pom.xml /build/
#copy the source code to the image
COPY src /build/src/
#set the working directory to the build folder
WORKDIR /build/
#build the project
RUN mvn package

FROM openjdk:17-slim
#copy the jar file from the maven build image to the current image
COPY --from=MAVEN_BUILD /build/target/*.jar /app.jar
#set the working directory to the current image
WORKDIR /
#run the jar file
ENTRYPOINT ["java","-jar","/app.jar"]
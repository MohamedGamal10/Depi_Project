FROM jenkins/jenkins:jdk17

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# change the group id from 999 to id in host machine
RUN groupadd -g 999 docker  


RUN usermod -aG docker jenkins

RUN chown -R jenkins:jenkins /var/jenkins_home && \
    chmod -R 775 /var/jenkins_home

USER jenkins

CMD ["jenkins"]

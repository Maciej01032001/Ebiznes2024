FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ = "Europe/Warsaw"

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.8

#RUN apt-get install -y openjdk-8-jdk
#RUN apt-get install -y curl zip unzip
#RUN curl -s "https://get.sdkman.io" | bash
#RUN /bin/bash -c "source $HOME/.sdkman/bin/sdkman-init.sh"
#RUN /bin/bash -c "source $HOME/.sdkman/bin/sdkman-init.sh && sdk install kotlin"

#RUN /bin/bash -c "source $HOME/.sdkman/bin/sdkman-init.sh && sdk install gradle"



EXPOSE 8080
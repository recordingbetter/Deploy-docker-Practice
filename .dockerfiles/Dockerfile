
FROM        eb_ubuntu
MAINTAINER  recordingbetter@gmail.com

# 현재 경로의 모든 파일들을 컨테이너의 /srv/deploy_eb/docker 폴더에 복사
COPY        . /srv/deploy_eb_docker
# cd /srv/deploy_eb/docker 와 같음
WORKDIR     /srv/deploy_eb_docker
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install -r .requirements/debug.txt

#RUN         uwsgi --http :8000 --chdir /srv/deploy_ec2/django_app --home /root/.pyenv/versions/deploy_eb_docker -w config.settings.debug

# supervisor 파일 복사
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/

CMD         supervisord -n

# 80포트와 8000포트를 열어줌
EXPOSE      80 8000

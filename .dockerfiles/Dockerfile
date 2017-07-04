
FROM        eb_ubuntu
MAINTAINER  recordingbetter@gmail.com

# 현재 경로의 모든 파일들을 컨테이너의 /srv/deploy_eb/docker 폴더에 복사
COPY        . /srv/deploy_eb_docker
# cd /srv/deploy_eb/docker 와 같음
WORKDIR     /srv/deploy_eb_docker

# requiremments.txt 설치
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install -r .requirements/deploy.txt

# .config/supervisor/uwsgi.conf로 이동
#RUN         uwsgi --http :8000 --chdir /srv/deploy_ec2/django_app --home /root/.pyenv/versions/deploy_eb_docker -w config.settings.debug

# supervisor 파일 복사
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d/


# nginx 설정파일, nginx 사이트 파일 복사
COPY        .config/nginx/nginx.conf /etc/nginx/
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/

# nginx 링크 작성
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx.conf
RUN         rm -rf /etc/nginx/sites-enabled/default

CMD         supervisord -n
# 80포트와 8000포트를 열어줌
EXPOSE      80 8000

FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY ./ /app
WORKDIR /app/
RUN pip install -r requirements.txt
RUN python build_database.py
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y --allow-unauthenticated yarn
RUN apt-get install -y nodejs
WORKDIR /app/relop-client/
RUN yarn install && yarn build
FROM node:14

RUN mkdir -p /home/node/app
WORKDIR /home/node/app
COPY ./src/ .
RUN npm install
RUN npm install lodash@4.15.0
ENV JWT_SECRET_KEY="3k1nvEbuSCQd4XXsnd0GWpBz9tpJLAOS"
RUN echo "ISITDTU{4d7a17cac68f1455cff829a52406acee}" > flag
RUN chmod -R 777 /home/node/app
USER node
EXPOSE 3000

CMD [ "node", "index.js" ]
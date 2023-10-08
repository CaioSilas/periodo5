FROM node

WORKDIR /usr/src/app


RUN npm init -y
RUN npm install kafkajs

COPY . .

CMD ["node", "./produtor.js"]
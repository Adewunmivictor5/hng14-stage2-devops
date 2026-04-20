FROM node:18-alpine

WORKDIR /app

RUN addgroup app && adduser -S -G app app

COPY package*.json ./
RUN npm install

COPY . .

USER app

EXPOSE 3000

HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

CMD ["npm", "start"]

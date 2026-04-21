# ---- Builder ----
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# ⚠️ No build step because your project doesn't have one

# ---- Production ----
FROM node:18-alpine

WORKDIR /app

RUN addgroup -S app && adduser -S app -G app

COPY --from=builder /app ./

USER app

EXPOSE 3000

CMD ["npm", "start"]

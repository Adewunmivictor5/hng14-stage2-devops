# ---- Builder Stage ----
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# ---- Production Stage ----
FROM node:18-alpine

WORKDIR /app

RUN apk add --no-cache wget

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

ENV NODE_ENV=production

# ✅ FIXED: copy correct path (NOT /app ./app)
COPY --from=builder /app /app

# install production deps in final image (IMPORTANT for HNG stability)
RUN npm ci --omit=dev

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
CMD wget -qO- http://localhost:3000 || exit 1

CMD ["npm", "start"]

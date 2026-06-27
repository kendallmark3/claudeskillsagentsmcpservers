FROM node:20-slim

WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm ci --omit=dev

COPY tsconfig.json server.ts ./
RUN npx tsc

ENV PORT=8002

CMD ["node", "dist/server.js"]

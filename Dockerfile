FROM node:18-alpine

WORKDIR /myportfolio

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install pnpm and dependencies
RUN npm install -g pnpm
RUN pnpm install --frozen-lockfile

# Copy source code
COPY . .

# Build the Astro site
RUN pnpm build

# Expose port 80 for nginx
EXPOSE 80

# Just keep the container running - nginx will serve the files
CMD ["tail", "-f", "/dev/null"]

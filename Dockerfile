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

# Install serve to host static files
RUN npm install -g serve

# Expose port 4321 (Astro's default)
EXPOSE 4321

# Serve the built static files with SPA mode
CMD ["serve", "-s", "dist", "-l", "4321", "--single"]

# Solo Leveling Goal Tracker App

A gamified goal tracking application inspired by the Solo Leveling manhwa/novel, designed to help users achieve their goals with AI-powered guidance and an RPG-style progression system.

## Features

- **AI-Powered Goal Analysis**: Get personalized learning plans based on your current skill level and aspirations
- **Hunter Rank System**: Progress from E-rank to S-rank in different domains as you complete tasks
- **Daily Task Generation**: Receive customized daily tasks that align with your goals and available time
- **XP and Level System**: Earn experience points for completing tasks and level up your character
- **Progress Visualization**: Track your growth and see how close you are to reaching the next rank
- **AI Coaching**: Get advice and feedback from an AI coach to help you stay on track

## Tech Stack

- **Frontend**: Next.js 14 with TypeScript, Tailwind CSS, shadcn/ui
- **Backend**: Next.js API Routes
- **Database**: MongoDB with Mongoose
- **Authentication**: NextAuth.js
- **AI Integration**: OpenAI GPT, HuggingFace

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- MongoDB Atlas account (or local MongoDB instance)
- OpenAI API key (for AI features)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/solo-leveling-app.git
   cd solo-leveling-app
   ```

2. Install dependencies
   ```bash
   npm install
   ```

3. Create a `.env.local` file in the root directory with the following variables:
   ```
   # MongoDB
   MONGODB_URI=your-mongodb-connection-string

   # NextAuth
   NEXTAUTH_URL=http://localhost:3000
   NEXTAUTH_SECRET=your-nextauth-secret-key

   # OAuth Providers (Optional)
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   GITHUB_ID=your-github-id
   GITHUB_SECRET=your-github-secret

   # AI Providers
   OPENAI_API_KEY=your-openai-api-key
   HUGGINGFACE_API_KEY=your-huggingface-api-key
   ```

4. Run the development server
   ```bash
   npm run dev
   ```

5. Open [http://localhost:3000](http://localhost:3000) in your browser

## Project Structure

- `/app`: Main application routes and pages
- `/components`: Reusable React components
- `/lib`: Utility functions and services
  - `/lib/ai`: AI-related services
  - `/lib/db`: Database models and connection utilities
- `/types`: TypeScript type definitions

## Hunter Rank System

The application uses a ranking system inspired by Solo Leveling:

- **E Rank**: Beginner level, starting point for most users
- **D Rank**: Basic proficiency achieved
- **C Rank**: Intermediate level with solid understanding
- **B Rank**: Advanced practitioner
- **A Rank**: Expert level
- **S Rank**: Mastery level

Each rank requires completing specific challenges and earning a minimum amount of XP to progress.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Inspired by the Solo Leveling manhwa/novel by Chugong
- UI components from shadcn/ui
- AI capabilities powered by OpenAI and HuggingFace 
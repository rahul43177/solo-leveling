# Solo Leveling Goal Tracker App - Architecture Document

## 1. System Architecture Overview

### 1.1 High-Level Architecture

This application follows a modern client-server architecture with the following key components:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  React Frontend │────▶│  FastAPI Backend│────▶│  PostgreSQL DB  │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │                       │                       │
        ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│    UI Layer     │     │   AI Services   │     │   pgvector      │
│                 │     │                 │     │   Extension     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

### 1.2 Technology Stack

**Frontend**:
- ReactJS with TypeScript
- Tailwind CSS with shadcn/ui components
- Redux for global state management
- React Router for routing
- Axios for API communication

**Backend**:
- Python FastAPI
- SQLAlchemy ORM
- JWT Authentication
- Pydantic for data validation

**Database**:
- PostgreSQL
- pgvector extension for vector embeddings

**AI Integration**:
- OpenAI API / Hugging Face Inference API
- Vector embeddings for semantic search
- Prompt engineering for specialized AI services

**DevOps**:
- Docker for containerization
- GitHub Actions for CI/CD
- Netlify/Vercel for frontend hosting
- AWS/GCP for backend hosting

## 2. Detailed Component Architecture

### 2.1 Frontend Architecture

#### 2.1.1 Component Hierarchy

```
App
├── Auth
│   ├── Login
│   ├── Register
│   └── ProfileSettings
├── Goals
│   ├── GoalsList
│   ├── GoalCreation
│   ├── GoalDetail
│   └── MilestoneProgress
├── Dashboard
│   ├── UserStats
│   ├── RankDisplay
│   ├── DailyTasksList
│   ├── ProgressCharts
│   └── Achievements
├── Tasks
│   ├── TaskItem
│   ├── TaskCompletion
│   └── TaskFeedback
├── AI Interactions
│   ├── GoalAssessment
│   ├── RankEvaluation
│   └── AICoaching
└── Shared Components
    ├── Navigation
    ├── Notifications
    ├── UI Elements
    └── ErrorBoundary
```

#### 2.1.2 State Management

- Redux store with the following slices:
  - `auth`: User authentication state
  - `goals`: User goals and milestones
  - `tasks`: Daily tasks and completion status
  - `progress`: XP, level, and rank tracking
  - `ai`: AI interaction history and contexts

#### 2.1.3 Routing Structure

```
/                       - Home/Landing page
/login                  - User login
/register               - User registration
/dashboard              - Main user dashboard
/goals                  - Goals list
/goals/new              - Goal creation
/goals/:id              - Goal details
/goals/:id/assessment   - Goal assessment
/goals/:id/milestones   - Milestone tracking
/tasks                  - Daily tasks
/tasks/:id              - Task details
/profile                - User profile
/settings               - User settings
```

### 2.2 Backend Architecture

#### 2.2.1 Service Layer

```
FastAPI App
├── Authentication Service
├── User Service
├── Goal Service
├── Task Service
├── Progress Service
├── AI Service
│   ├── Goal Analysis
│   ├── Rank Assessment
│   ├── Task Generation
│   ├── Progress Adaptation
│   └── Coaching
└── Notification Service
```

#### 2.2.2 API Endpoints

**Authentication Endpoints**:
- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/refresh-token`
- `POST /api/auth/logout`

**User Endpoints**:
- `GET /api/users/{user_id}`
- `PUT /api/users/{user_id}`
- `GET /api/users/{user_id}/stats`
- `PUT /api/users/{user_id}/settings`

**Goal Endpoints**:
- `GET /api/goals`
- `POST /api/goals`
- `GET /api/goals/{goal_id}`
- `PUT /api/goals/{goal_id}`
- `DELETE /api/goals/{goal_id}`
- `GET /api/goals/{goal_id}/milestones`

**Task Endpoints**:
- `GET /api/tasks`
- `GET /api/tasks/daily`
- `GET /api/tasks/{task_id}`
- `PUT /api/tasks/{task_id}`
- `POST /api/tasks/{task_id}/complete`
- `POST /api/tasks/{task_id}/feedback`

**AI Endpoints**:
- `POST /api/ai/analyze-goal`
- `POST /api/ai/assess-skill`
- `POST /api/ai/generate-tasks`
- `POST /api/ai/adapt-plan`
- `POST /api/ai/coaching`

#### 2.2.3 Middleware

- Authentication middleware
- Request logging middleware
- Error handling middleware
- Rate limiting middleware
- CORS middleware

### 2.3 AI Service Architecture

#### 2.3.1 AI System Components

```
┌────────────────────────┐
│    AI Service Layer    │
└────────────────────────┘
          │
┌─────────┴─────────────┐
▼                       ▼
┌────────────────┐      ┌────────────────┐
│ Prompt Manager │      │ Response Parser│
└────────────────┘      └────────────────┘
          │                     │
          ▼                     ▼
┌────────────────┐      ┌────────────────┐
│  LLM Service   │─────▶│  Validation    │
└────────────────┘      └────────────────┘
          │                     │
          ▼                     ▼
┌────────────────┐      ┌────────────────┐
│Vector DB Service│     │  Knowledge Base│
└────────────────┘      └────────────────┘
```

#### 2.3.2 AI Service Interfaces

**Goal Analysis Service**:
- Input: User goal description, domain, time availability
- Process: Structure goal into milestones and tasks, assess current rank
- Output: Structured plan with milestones, tasks, rank assessment

**Rank Assessment Service**:
- Input: User responses to domain-specific questions
- Process: Evaluate responses against domain knowledge base
- Output: Current rank, explanation, progression path

**Task Generation Service**:
- Input: User goal plan, current rank, available time
- Process: Generate appropriate daily tasks
- Output: Structured daily tasks with difficulty, XP, time estimates

**Progress Adaptation Service**:
- Input: User performance metrics, feedback
- Process: Adjust plan difficulty, pacing, focus areas
- Output: Adapted plan with modifications

**Coaching Service**:
- Input: User progress, struggles, achievements
- Process: Generate personalized coaching messages
- Output: Motivational and instructional content

## 3. Database Schema

### 3.1 Entity-Relationship Diagram

```
┌─────────┐     ┌──────────────┐     ┌─────────┐
│  Users  │─────│ User_Domains │─────│ Domains │
└─────────┘     └──────────────┘     └─────────┘
     │                                     │
     │                                     │
     ▼                                     ▼
┌─────────┐     ┌──────────────┐     ┌─────────────┐
│  Goals  │─────│  Milestones  │     │Rank_Systems │
└─────────┘     └──────────────┘     └─────────────┘
     │                │
     │                │
     ▼                ▼
┌─────────┐     ┌──────────────┐     ┌─────────────────┐
│  Tasks  │─────│Task_Activities│     │AI_Interactions  │
└─────────┘     └──────────────┘     └─────────────────┘
     │                                     │
     └─────────────────┬───────────────────┘
                       │
                       ▼
                 ┌───────────┐
                 │Embeddings │
                 └───────────┘
```

### 3.2 Table Details

The database consists of 10 tables, as defined in the specification:

1. **Users** - Stores user account information and profile data
2. **Domains** - Represents different areas of expertise/skills
3. **User_Domains** - Junction table tracking user progress in specific domains
4. **Goals** - Stores user-created goals with AI-generated plans
5. **Milestones** - Breakdown of goals into achievement milestones
6. **Tasks** - Daily actionable items for users to complete
7. **Rank_Systems** - Domain-specific ranking criteria and progression paths
8. **AI_Interactions** - Record of user interactions with AI systems
9. **Task_Activities** - History of user actions on tasks
10. **Embeddings** - Vector representations for semantic search

### 3.3 Key Relationships

- A user can have multiple goals
- A goal belongs to a single domain and user
- A goal has multiple milestones
- A milestone has multiple tasks
- A task belongs to a goal, milestone, and user
- A user has rank progress in multiple domains

## 4. Key System Workflows

### 4.1 Goal Creation and Assessment Flow

```
┌──────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐
│  User    │    │ Frontend  │    │  Backend  │    │    AI     │
└────┬─────┘    └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
     │                │                │                │
     │ Enter Goal     │                │                │
     │─────────────> │                │                │
     │                │                │                │
     │                │ Request Analysis               │
     │                │─────────────────────────────> │
     │                │                │                │
     │                │                │  Process Goal  │
     │                │                │ <─────────────│
     │                │                │                │
     │                │ Return Structured Plan         │
     │                │ <─────────────────────────────│
     │                │                │                │
     │ Display Plan   │                │                │
     │ <─────────────│                │                │
     │                │                │                │
     │ Confirm Plan   │                │                │
     │─────────────> │                │                │
     │                │ Save Goal & Plan               │
     │                │─────────────> │                │
     │                │                │                │
     │                │ Generate Assessment Questions  │
     │                │─────────────────────────────> │
     │                │                │                │
     │ Show Questions │                │                │
     │ <─────────────│                │                │
     │                │                │                │
     │ Submit Answers │                │                │
     │─────────────> │ Process Assessment             │
     │                │─────────────────────────────> │
     │                │                │                │
     │                │ Return Rank & Path            │
     │                │ <─────────────────────────────│
     │                │                │                │
     │ Display Rank   │                │                │
     │ <─────────────│                │                │
     │                │                │                │
```

### 4.2 Daily Task Generation and Completion

```
┌──────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐
│  User    │    │ Frontend  │    │  Backend  │    │    AI     │
└────┬─────┘    └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
     │                │                │                │
     │ Open Dashboard │                │                │
     │─────────────> │                │                │
     │                │ Request Tasks  │                │
     │                │─────────────> │                │
     │                │                │                │
     │                │                │ Generate Tasks │
     │                │                │─────────────> │
     │                │                │                │
     │                │                │ Return Tasks   │
     │                │                │ <─────────────│
     │                │                │                │
     │                │ Return Tasks   │                │
     │                │ <─────────────│                │
     │                │                │                │
     │ Display Tasks  │                │                │
     │ <─────────────│                │                │
     │                │                │                │
     │ Complete Task  │                │                │
     │─────────────> │                │                │
     │                │ Update Status  │                │
     │                │─────────────> │                │
     │                │                │                │
     │                │ Update XP/Level│                │
     │                │ <─────────────│                │
     │                │                │                │
     │ Show Progress  │                │                │
     │ <─────────────│                │                │
     │                │                │                │
     │ Provide Feedback                │                │
     │─────────────> │ Send Feedback  │                │
     │                │─────────────> │                │
     │                │                │                │
     │                │                │ Adapt Plan     │
     │                │                │─────────────> │
     │                │                │                │
     │                │                │ Return Updates │
     │                │                │ <─────────────│
     │                │                │                │
```

## 5. AI Implementation Details

### 5.1 Prompt Engineering

Each AI service requires specialized prompts to achieve the desired output:

#### 5.1.1 Goal Analysis Prompt

The system uses a structured prompt template for goal analysis:

```
You are an AI assistant for a Solo Leveling inspired goal-tracking app. Your task is to analyze the user's goal and create a structured plan.

User Goal: "{userGoal}"
User's Current Level: "{currentLevel}" (if available)
Available Time: {availableTimePerDay} minutes per day
Domain: {domain}

Please create:
1. A structured breakdown of this goal into 3-5 milestones
2. For each milestone, create 3-7 specific, actionable tasks
3. Estimate the time required for each task (in minutes)
4. Assign an appropriate difficulty level (1-10) for each task
5. For the domain of this goal, assess what Hunter Rank (E through S) the user currently has based on their reported knowledge
6. Create a clear progression path showing what they need to achieve to advance to each higher rank

Format your response as a structured JSON object with the following schema:
{
  "milestones": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "tasks": [
        {
          "id": "string",
          "title": "string",
          "description": "string",
          "type": "string",
          "difficulty": number,
          "estimatedTimeMinutes": number,
          "xpReward": number,
          "resources": []
        }
      ]
    }
  ],
  "currentRank": "string",
  "targetRank": "string",
  "progressionPath": {
    "ranks": [
      {
        "rank": "string",
        "requirements": "string",
        "estimatedDuration": "string"
      }
    ]
  },
  "estimatedCompletionTimeDays": number
}
```

#### 5.1.2 Rank Assessment Prompt

Specialized prompt for rank assessment:

```
You are an AI assistant for a Solo Leveling inspired goal-tracking app. Your task is to assess the user's current skill level in {domain}.

Based on the following information provided by the user:
{userResponses}

Please:
1. Assess their current knowledge/skill level
2. Assign an appropriate Hunter Rank (E through S)
3. Explain why they received this rank
4. Identify knowledge gaps they need to fill
5. Suggest a progression path to the next rank

Format your response as a structured JSON object with the following schema:
{
  "currentRank": "string",
  "explanation": "string",
  "knowledgeGaps": ["string"],
  "nextRank": "string",
  "requiredSkills": ["string"],
  "recommendedFocus": "string",
  "estimatedTimeToNextRank": "string"
}
```

### 5.2 Domain Knowledge Bases

The system maintains structured knowledge bases for popular domains:

#### 5.2.1 Knowledge Base Structure

Each domain knowledge base includes:
- Rank definitions (E through S)
- Required skills for each rank
- Assessment questions
- Common learning paths
- Task templates

#### 5.2.2 Sample React Development Knowledge Base

```json
{
  "domain": "React Development",
  "ranks": [
    {
      "name": "E",
      "description": "Complete beginner with basic HTML/CSS knowledge",
      "skills": [
        "Basic HTML understanding",
        "CSS familiarity",
        "JavaScript fundamentals"
      ],
      "assessmentQuestions": [
        {
          "question": "Have you used HTML and CSS before?",
          "type": "multiple_choice",
          "options": ["Never", "A little", "Regularly", "Expert level"]
        },
        {
          "question": "How comfortable are you with JavaScript?",
          "type": "multiple_choice",
          "options": ["Not at all", "Basic understanding", "Comfortable", "Very proficient"]
        }
      ],
      "taskTemplates": [
        {
          "type": "learning",
          "title": "Complete HTML/CSS basics course",
          "difficultyRange": [1, 3],
          "timeRange": [30, 60]
        }
      ]
    },
    {
      "name": "D",
      "description": "Beginner with basic React concepts",
      "skills": [
        "React component basics",
        "Props and state",
        "Basic hooks (useState, useEffect)",
        "JSX syntax"
      ],
      "assessmentQuestions": [
        {
          "question": "Have you built any React applications before?",
          "type": "multiple_choice",
          "options": ["Never", "Very simple ones", "A few small projects", "Several complex projects"]
        },
        {
          "question": "Which React hooks have you used?",
          "type": "multiple_select",
          "options": ["useState", "useEffect", "useContext", "useReducer", "useCallback", "useMemo", "None"]
        }
      ],
      "taskTemplates": [
        {
          "type": "learning",
          "title": "Complete React basics tutorial",
          "difficultyRange": [2, 4],
          "timeRange": [45, 90]
        },
        {
          "type": "practice",
          "title": "Build a simple todo app with React",
          "difficultyRange": [3, 5],
          "timeRange": [60, 120]
        }
      ]
    }
  ]
}
```

### 5.3 AI Response Processing

The system implements structured processing of AI responses:

1. **Validation**: Ensure JSON responses match the expected schema
2. **Enrichment**: Add system-generated IDs, timestamps, etc.
3. **Sanitization**: Remove potentially problematic content
4. **Storage**: Save processed responses to the database
5. **Translation**: Map AI response fields to application models

## 6. Gamification System Architecture

### 6.1 XP and Level System

- XP points awarded for task completion based on:
  - Task difficulty (1-10 scale)
  - Completion quality (based on feedback)
  - Streak bonuses (consecutive days)
- Level progression follows a curve:
  - `XP_for_next_level = base_xp * (current_level ^ 1.5)`
- Level-up events trigger:
  - UI celebrations
  - Achievement unlocks
  - New task difficulty adjustments

### 6.2 Rank Progression System

- Hunter Ranks from E (lowest) to S (highest):
  - E Rank: Beginner
  - D Rank: Basic understanding
  - C Rank: Intermediate
  - B Rank: Advanced
  - A Rank: Expert
  - S Rank: Master
- Rank advancement requires:
  - Completing milestone tasks
  - Passing assessment challenges ("boss battles")
  - Demonstrating required skills through feedback

### 6.3 Achievement System

- Achievements awarded for:
  - Completing streaks (3-day, 7-day, 30-day)
  - Reaching milestones
  - Rank advancements
  - Task completion metrics (speed, quality)
- Achievement display on user dashboard
- Achievement history tracking

## 7. Security Architecture

### 7.1 Authentication and Authorization

- JWT-based authentication flow
- Token refresh mechanism
- Role-based access control:
  - User role (standard access)
  - Admin role (system management)
- Password storage using bcrypt hashing
- Multi-factor authentication (future implementation)

### 7.2 Data Protection

- All API endpoints secured with authentication
- Rate limiting on sensitive endpoints
- Input validation using Pydantic models
- PostgreSQL connection security
- API call logging for auditing

### 7.3 AI Security Considerations

- Prompt injection prevention
- User data isolation in AI contexts
- Approval workflows for AI-generated content
- Fallback mechanisms for AI service failures
- Rate limiting for AI API calls

## 8. Integration Points

### 8.1 External Service Integrations

- OpenAI API integration for LLM capabilities
- Alternative integration with Hugging Face Inference API
- OAuth providers for social login (future)
- Email service for notifications
- Analytics service for usage tracking

### 8.2 Mobile Integration Planning

- RESTful API designed for mobile consumption
- Authentication flows compatible with mobile apps
- Push notification endpoints
- Offline-first data handling plans
- API versioning strategy

## 9. Deployment Architecture

### 9.1 Development Environment

```
┌─────────────────────────────────────────┐
│             Docker Compose              │
├─────────────┬─────────────┬─────────────┤
│  Frontend   │   Backend   │  Database   │
│  Container  │  Container  │  Container  │
│  (React)    │  (FastAPI)  │ (PostgreSQL)│
└─────────────┴─────────────┴─────────────┘
```

### 9.2 Production Environment

```
┌─────────────┐          ┌─────────────┐
│   Netlify/  │          │    AWS/GCP  │
│   Vercel    │          │             │
├─────────────┤          ├─────────────┤
│  Frontend   │◄────────►│   Backend   │
│  (React)    │          │  (FastAPI)  │
└─────────────┘          └─────────────┘
                               │
                               ▼
                         ┌─────────────┐
                         │  Managed DB │
                         │ (PostgreSQL)│
                         └─────────────┘
                               │
                               ▼
                         ┌─────────────┐
                         │  OpenAI API │
                         │             │
                         └─────────────┘
```

### 9.3 CI/CD Pipeline

- GitHub Actions for automated testing and deployment
- Staging environment for pre-production testing
- Automated database migrations
- Blue-green deployment strategy
- Rollback procedures

## 10. Performance Considerations

### 10.1 Database Optimization

- Indexing strategy for frequently queried fields
- Connection pooling
- Query optimization for common patterns
- PostgreSQL tuning for vector operations
- Caching layer for frequently accessed data

### 10.2 API Performance

- Response compression
- Pagination for list endpoints
- Partial responses for large resources
- Background processing for long-running operations
- AI response caching where appropriate

### 10.3 Frontend Performance

- Code splitting and lazy loading
- Asset optimization
- Client-side caching
- Progressive loading for dashboard components
- Web vitals monitoring

## 11. Scalability Planning

### 11.1 Horizontal Scaling

- Stateless backend design for horizontal scaling
- Database read replicas for scaling read operations
- Load balancing configuration
- Session management without sticky sessions

### 11.2 Vertical Scaling

- Resource requirements by component:
  - Frontend: Minimal (static hosting)
  - Backend: Medium (dependent on concurrent users)
  - Database: High (grows with user data)
  - AI Services: High (dependent on request volume)

### 11.3 Cost Management

- AI API cost optimization strategies
- Database storage tier planning
- Caching to reduce API calls
- Resource scaling based on usage patterns

## 12. Monitoring and Analytics

### 12.1 System Monitoring

- API endpoint performance tracking
- Error rate monitoring
- Database performance metrics
- AI service response times
- Infrastructure health checks

### 12.2 User Analytics

- Task completion rates
- User engagement metrics
- Goal achievement timelines
- AI service effectiveness
- Feature usage tracking

## 13. Implementation Roadmap

### 13.1 Phase 1: Core Infrastructure (Weeks 1-3)
- Set up project repositories
- Configure development environments
- Implement database schema
- Create basic API endpoints
- Set up authentication

### 13.2 Phase 2: AI Foundation (Weeks 3-6)
- Implement AI service integrations
- Develop prompt templates
- Create knowledge bases
- Build response processing

### 13.3 Phase 3: Core Features (Weeks 6-10)
- Build goal creation flow
- Implement task system
- Develop dashboard
- Create rank assessment

### 13.4 Phase 4: Gamification (Weeks 10-13)
- Implement XP system
- Build level progression
- Develop achievements
- Create rank advancement

### 13.5 Phase 5: Polish and Testing (Weeks 13-16)
- UI refinement
- Performance optimization
- User testing
- Bug fixes

### 13.6 Phase 6: Deployment (Weeks 16-18)
- Production environment setup
- CI/CD pipeline
- Monitoring configuration
- Launch preparation

## 14. Future Expansion Plans

### 14.1 Mobile Applications
- iOS app development
- Android app development
- Cross-platform considerations

### 14.2 Advanced AI Features
- Voice interaction
- Image recognition for task proof
- Personalized content recommendations
- Advanced progress prediction

### 14.3 Social Features
- Group goals
- Mentorship system
- Achievements sharing
- Competition system

### 14.4 Enterprise Integration
- Team goals
- Manager dashboards
- Learning path templates
- Integration with learning management systems 
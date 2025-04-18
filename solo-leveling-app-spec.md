# Solo Leveling Goal Tracker App with AI Integration - Comprehensive Development Guide

## Project Overview
I want to build a gamified goal tracking application inspired by the Solo Leveling anime/manga. The core concept is to help users achieve their goals through a gamified experience where they "level up" as they make progress. A crucial component is the AI integration that helps users structure their goals, assess their current level, and create personalized progression paths. I'm starting with a web application first, with plans to expand to mobile (iOS and Android) later.

## Core Features

### User Goal Management
- Users can create goals with brief or detailed descriptions
- Users can set deadlines for their goals
- Multiple goals can be tracked simultaneously
- AI-powered goal structuring and breakdown

### AI-Powered Planning System
- AI converts brief goal descriptions into structured plans
- Assesses user's current skill/knowledge level in a domain (like a React developer's skill level)
- Assigns appropriate "Hunter Rank" (E through S rank) based on assessment
- Creates progression paths with specific tasks to advance ranks
- Adapts plans based on user's available time commitment
- Recommends daily tasks based on progression plan
- Adjusts plans based on user's progress feedback

### Task System
- AI-generated daily tasks based on the structured goal plan
- Users check off completed tasks
- Task completion grants XP
- Missing tasks results in penalties
- Task difficulty adjusted based on user's rank and progress

### Gamification Elements
- XP system for progress tracking
- Level progression based on accumulated XP
- Hunter Rank system (E through S ranks) for skill assessment
- Progress bars for visual feedback
- Penalties for missed tasks to create urgency
- "Boss battles" as milestone challenges between rank advancements

### User Experience
- Dashboard to visualize progress
- Daily task list
- Level/rank display
- Statistics and achievements
- AI insights and recommendations

## Tech Stack Requirements (Updated for Company Stack)

### Frontend
- **Framework**: ReactJS
- **UI Library**: Tailwind CSS with shadcn/ui components
- **State Management**: Redux or React Context API
- **Routing**: React Router
- **API Communication**: Axios or Fetch API

### Backend
- **Framework**: Python FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT with FastAPI auth libraries
- **API Documentation**: Swagger/OpenAPI (included with FastAPI)

### AI Integration
- **LLM API**: OpenAI API (limited free credits) or Hugging Face Inference API (free tier)
- **Alternative**: Self-hosted open-source models like Ollama (completely free but requires server)
- **Vector Database**: Pgvector extension for PostgreSQL or standalone Pinecone (free tier)
- **Embeddings**: OpenAI embeddings API or open-source alternatives

### Deployment
- **Frontend Hosting**: Netlify, Vercel, or company infrastructure
- **Backend Hosting**: Company infrastructure, AWS, or other cloud provider
- **Domain**: Initially use subdomain or company-provided domain
- **Version Control**: GitHub or company's Git server

## AI System Architecture & Design

### 1. Goal Analysis & Structuring System

This system will take a user's brief goal description and transform it into a structured plan.

**Implementation:**
- Create a specialized prompt template for goal analysis
- Use few-shot examples to teach the AI how to structure different types of goals
- Include domain-specific knowledge for popular goal categories (programming, fitness, language learning, etc.)
- Implement a feedback loop where users can refine AI-generated plans

**Example Flow:**
1. User enters: "I want to become proficient in React"
2. AI processes this input and requests additional information:
   - Current experience level with React
   - Specific areas of interest (web apps, mobile, etc.)
   - Available time commitment (hours per day/week)
   - Deadline or timeframe
3. AI generates a structured plan with:
   - Main goal broken into milestones
   - Each milestone broken into specific tasks
   - Estimated completion timeframes
   - Resources/references for each task
   - Success metrics for task completion

### 2. Rank Assessment System

This system evaluates the user's current skill/knowledge level in their goal domain and assigns an appropriate "Hunter Rank" (E through S).

**Implementation:**
- Create a knowledge base of skill assessment criteria for popular domains
- Design structured assessment questionnaires for different domains
- Develop ranking algorithms based on assessment responses
- Store domain-specific knowledge hierarchies for progression paths

**Example for React Developer Assessment:**
1. AI asks specific questions about React knowledge:
   - "Can you explain React's virtual DOM?"
   - "Have you worked with hooks? Which ones?"
   - "What state management solutions have you used?"
   - "Have you built authentication systems in React?"
2. Based on responses, AI assigns a rank:
   - E Rank: Complete beginner (HTML/CSS knowledge only)
   - D Rank: Basic React concepts (components, props, basic hooks)
   - C Rank: Intermediate (Custom hooks, Context API, basic routing)
   - B Rank: Advanced (Complex state management, performance optimization)
   - A Rank: Expert (Advanced patterns, architecture, teaching ability)
   - S Rank: Master (Deep framework understanding, contribution-level knowledge)

### 3. Task Generation System

This system creates daily tasks that align with the user's goal plan, current rank, and available time.

**Implementation:**
- Create templates for different task types (learning, practice, project work, review)
- Develop algorithms for task sequencing based on dependencies
- Implement time-boxing based on user's available hours
- Design adaptive difficulty scaling based on user progress

**Example Task Generation:**
1. For a D-Rank React learner with 2 hours daily:
   - Day 1 Task: "Complete tutorial on useEffect hook (45 min) + Build a simple weather app using the hook (1 hour 15 min)"
   - Task difficulty: Appropriate for D-Rank
   - XP reward: 200 XP
   - Resources: Links to recommended tutorials or documentation

### 4. Progress Tracking & Adaptation System

This system monitors user progress and adapts plans based on performance and feedback.

**Implementation:**
- Design progress tracking metrics (completion rate, speed, accuracy)
- Create feedback collection mechanisms after task completion
- Develop plan adjustment algorithms based on performance data
- Implement milestone assessments for rank advancement

**Example Adaptation:**
1. If user completes tasks faster than expected:
   - Increase task difficulty
   - Add more advanced concepts
   - Accelerate progress toward next rank
2. If user struggles with certain tasks:
   - Provide additional foundational tasks
   - Decrease complexity temporarily
   - Offer alternative learning approaches

### 5. AI Conversation & Coaching System

This system provides conversational guidance and motivational support.

**Implementation:**
- Design a coaching persona with appropriate tone and style
- Create conversation templates for different user situations (struggling, excelling, returning after absence)
- Implement motivation techniques based on user progress patterns
- Develop personalized insights based on performance data

**Example Interactions:**
1. For struggling users:
   - "I've noticed you're finding the Redux tasks challenging. Would you like to try an alternative approach first? Context API might be more approachable before moving to Redux."
2. For returning users:
   - "Welcome back! It's been 5 days since you last completed a task. Let's start with a quick review of React hooks before continuing with your plan."

## Database Schema (PostgreSQL)

### 1. Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    join_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    current_xp INTEGER NOT NULL DEFAULT 0,
    current_level INTEGER NOT NULL DEFAULT 1,
    settings JSONB NOT NULL DEFAULT '{
        "availableTimePerDay": 60,
        "notificationPreferences": {
            "email": true,
            "push": false
        }
    }'
);
```

### 2. Domains Table
```sql
CREATE TABLE domains (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);
```

### 3. User_Domains Table
```sql
CREATE TABLE user_domains (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    domain_id INTEGER REFERENCES domains(id) ON DELETE CASCADE,
    current_rank VARCHAR(1) NOT NULL DEFAULT 'E',
    rank_progress FLOAT NOT NULL DEFAULT 0,
    expertise JSONB,
    UNIQUE(user_id, domain_id)
);
```

### 4. Goals Table
```sql
CREATE TABLE goals (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    domain_id INTEGER REFERENCES domains(id) ON DELETE SET NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deadline TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    ai_generated_plan JSONB
);
```

### 5. Milestones Table
```sql
CREATE TABLE milestones (
    id SERIAL PRIMARY KEY,
    goal_id INTEGER REFERENCES goals(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    sequence_order INTEGER NOT NULL
);
```

### 6. Tasks Table
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    goal_id INTEGER REFERENCES goals(id) ON DELETE CASCADE,
    milestone_id INTEGER REFERENCES milestones(id) ON DELETE SET NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    type VARCHAR(50) NOT NULL,
    difficulty INTEGER NOT NULL CHECK (difficulty BETWEEN 1 AND 10),
    estimated_time_minutes INTEGER NOT NULL,
    xp_reward INTEGER NOT NULL,
    penalty_for_missing INTEGER NOT NULL DEFAULT 0,
    due_date TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    completed_at TIMESTAMP,
    resources JSONB,
    feedback JSONB
);
```

### 7. Rank_Systems Table
```sql
CREATE TABLE rank_systems (
    id SERIAL PRIMARY KEY,
    domain_id INTEGER REFERENCES domains(id) ON DELETE CASCADE,
    ranks JSONB NOT NULL
);
```

### 8. AI_Interactions Table
```sql
CREATE TABLE ai_interactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    goal_id INTEGER REFERENCES goals(id) ON DELETE SET NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    type VARCHAR(50) NOT NULL,
    user_input TEXT,
    ai_response TEXT,
    context JSONB,
    feedback_rating INTEGER
);
```

### 9. Task_Activities Table
```sql
CREATE TABLE task_activities (
    id SERIAL PRIMARY KEY,
    task_id INTEGER REFERENCES tasks(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    activity_type VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    details JSONB
);
```

### 10. Vector Table (using pgvector extension)
```sql
-- Install pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create table for embeddings
CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    content_type VARCHAR(50) NOT NULL,
    content_id INTEGER NOT NULL,
    embedding vector(1536),  -- Adjust dimension based on embedding model
    metadata JSONB
);

-- Create index for vector similarity search
CREATE INDEX embedding_idx ON embeddings USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

## Development Approach (Step by Step)

### Phase 1: Project Setup and Foundation
1. Set up React frontend project with create-react-app or Vite
2. Configure Tailwind CSS and shadcn/ui components
3. Set up FastAPI backend project structure
4. Configure PostgreSQL database and connection
5. Implement SQLAlchemy models based on schema
6. Set up JWT authentication in FastAPI
7. Create basic API endpoints and frontend routing

### Phase 2: AI System Development
1. Design and implement the goal analysis system
   - Create prompt templates
   - Implement parsing logic for AI responses 
   - Develop goal structuring algorithms
2. Build the rank assessment system
   - Create assessment questionnaires
   - Implement ranking algorithms
   - Design rank progression paths
3. Develop the task generation system
   - Create task templates
   - Implement scheduling algorithms
   - Design difficulty scaling logic
4. Create the progress tracking system
   - Implement metrics collection
   - Develop adaptation algorithms
   - Build feedback processing
5. Build the conversation system
   - Design coaching personas
   - Create conversation templates
   - Implement context management

### Phase 3: Core Application Functionality
1. Build user registration and login flows
2. Create goal creation interface with AI assistance
3. Implement the assessment conversation flow
4. Build the plan viewing and management interfaces
5. Create the daily task assignment and tracking system

### Phase 4: User Interface Development
1. Design and build the dashboard
   - Progress visualization components
   - Rank display elements
   - Task management interfaces
2. Create the conversation interface for AI coaching
3. Implement notifications and reminders
4. Build settings and preferences management
5. Create the achievement and milestone celebration screens

### Phase 5: Gamification Implementation
1. Design and implement the XP system
2. Create the level progression mechanics
3. Build the rank advancement challenges ("boss battles")
4. Implement penalties and streak systems
5. Add visual feedback and celebrations for achievements

### Phase 6: Testing and Optimization
1. Conduct user testing of AI interactions
2. Optimize prompts based on user feedback
3. Fine-tune task generation algorithms
4. Optimize database queries and indexing
5. Implement caching for AI responses
6. Add error handling and fallbacks for AI services

### Phase 7: Polish and Deployment
1. Add responsive design for all screen sizes
2. Implement dark/light mode
3. Add animations and transitions
4. Optimize performance
5. Deploy frontend and backend to production
6. Set up monitoring and analytics

## AI Implementation Details

### 1. Prompt Engineering

Create specialized prompts for different AI functions:

**Goal Analysis Prompt Template:**
```
You are an AI assistant for a Solo Leveling inspired goal-tracking app. Your task is to analyze the user's goal and create a structured plan.

User Goal: "{userGoal}"
User's Current Level: "{currentLevel}" (if available)
Available Time: {availableTimePerDay} minutes per day

Please create:
1. A structured breakdown of this goal into 3-5 milestones
2. For each milestone, create 3-7 specific, actionable tasks
3. Estimate the time required for each task (in minutes)
4. Assign an appropriate difficulty level (1-10) for each task
5. For the domain of this goal, assess what Hunter Rank (E through S) the user currently has based on their reported knowledge
6. Create a clear progression path showing what they need to achieve to advance to each higher rank

Format your response as a structured JSON object following this schema:
{schema details}
```

**Assessment Prompt Template:**
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

Format your response as a structured JSON object following this schema:
{schema details}
```

### 2. FastAPI AI Integration

Implement a robust AI service in FastAPI:

```python
# ai_service.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import openai
from typing import Dict, List, Optional
import json
import os

router = APIRouter()

class GoalAnalysisRequest(BaseModel):
    user_goal: str
    current_level: Optional[str] = None
    available_time_per_day: int
    domain: str

class AssessmentRequest(BaseModel):
    domain: str
    user_responses: Dict[str, str]

class StructuredPlan(BaseModel):
    milestones: List[Dict]
    current_rank: str
    target_rank: str
    progression_path: Dict
    estimated_completion_time_days: int

async def get_openai_client():
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client

@router.post("/analyze-goal", response_model=StructuredPlan)
async def analyze_goal(
    request: GoalAnalysisRequest,
    openai_client = Depends(get_openai_client)
):
    try:
        # Prepare prompt
        prompt = f"""
        You are an AI assistant for a Solo Leveling inspired goal-tracking app. Your task is to analyze the user's goal and create a structured plan.

        User Goal: "{request.user_goal}"
        User's Current Level: "{request.current_level or 'Not specified'}"
        Available Time: {request.available_time_per_day} minutes per day
        Domain: {request.domain}

        Please create:
        1. A structured breakdown of this goal into 3-5 milestones
        2. For each milestone, create 3-7 specific, actionable tasks
        3. Estimate the time required for each task (in minutes)
        4. Assign an appropriate difficulty level (1-10) for each task
        5. For the domain of this goal, assess what Hunter Rank (E through S) the user currently has based on their reported knowledge
        6. Create a clear progression path showing what they need to achieve to advance to each higher rank

        Format your response as a structured JSON object with the following fields:
        - milestones: array of milestone objects
        - current_rank: string (E through S)
        - target_rank: string (E through S)
        - progression_path: object with rank progression details
        - estimated_completion_time_days: integer
        """
        
        # Get response from OpenAI
        response = await openai_client.chat.completions.create(
            model="gpt-4-turbo",  # Use appropriate model
            messages=[
                {"role": "system", "content": "You are an AI goal structuring assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2000,
            response_format={"type": "json_object"}
        )
        
        # Parse and validate response
        result = json.loads(response.choices[0].message.content)
        
        # Process and validate the response here
        structured_plan = StructuredPlan(**result)
        return structured_plan
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")
```

### 3. React Frontend AI Integration

Create a service for interacting with the AI backend:

```typescript
// src/services/aiService.ts
import axios from 'axios';
import { GoalAnalysisRequest, StructuredPlan, AssessmentRequest, SkillAssessment } from '../types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const aiService = {
  async analyzeGoal(request: GoalAnalysisRequest): Promise<StructuredPlan> {
    try {
      const response = await axios.post(`${API_BASE_URL}/api/ai/analyze-goal`, request, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      });
      return response.data;
    } catch (error) {
      console.error('Error analyzing goal:', error);
      throw new Error('Failed to analyze goal. Please try again.');
    }
  },
  
  async assessSkill(request: AssessmentRequest): Promise<SkillAssessment> {
    try {
      const response = await axios.post(`${API_BASE_URL}/api/ai/assess-skill`, request, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      });
      return response.data;
    } catch (error) {
      console.error('Error assessing skill:', error);
      throw new Error('Failed to assess skill. Please try again.');
    }
  },
  
  // Additional AI service methods...
};
```

### 4. Domain-Specific Knowledge Base

Create structured knowledge bases in Python:

```python
# knowledge_base.py
from typing import List, Dict, Any

class DomainKnowledgeBase:
    def __init__(self):
        self.domains = {
            "React Development": self._react_development_knowledge(),
            "Python Programming": self._python_programming_knowledge(),
            "Fitness": self._fitness_knowledge(),
            # Additional domains...
        }
    
    def get_domain_knowledge(self, domain_name: str) -> Dict[str, Any]:
        """Get knowledge base for a specific domain"""
        return self.domains.get(domain_name, {})
    
    def get_assessment_questions(self, domain_name: str, rank: str = None) -> List[Dict[str, Any]]:
        """Get assessment questions for a domain and optional rank"""
        domain = self.domains.get(domain_name, {})
        if not domain:
            return []
        
        if rank:
            # Get questions specific to a rank
            for rank_info in domain.get("ranks", []):
                if rank_info["name"] == rank:
                    return rank_info.get("assessmentQuestions", [])
            return []
        else:
            # Get all questions for the domain
            questions = []
            for rank_info in domain.get("ranks", []):
                questions.extend(rank_info.get("assessmentQuestions", []))
            return questions
    
    def _react_development_knowledge(self) -> Dict[str, Any]:
        """Knowledge base for React Development"""
        return {
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
                        # More questions...
                    ]
                },
                # More ranks...
            ]
        }
    
    # Additional domain knowledge methods...
```

### 5. Progress Tracking and Adaptation

Implement progress tracking in FastAPI:

```python
# progress_service.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from pydantic import BaseModel

from database import get_db
from models import User, Goal, Task, TaskActivity
from ai_service import get_ai_client

router = APIRouter()

class ProgressData(BaseModel):
    user_id: int
    goal_id: int
    completion_rate: float
    average_time_ratio: float
    struggling_areas: List[str]

class AdaptedPlan(BaseModel):
    tasks: List[Dict[str, Any]]
    adaptations: List[Dict[str, Any]]

@router.post("/adapt-plan", response_model=AdaptedPlan)
async def adapt_plan(
    progress_data: ProgressData,
    db: Session = Depends(get_db),
    ai_client = Depends(get_ai_client)
):
    # Get the user's current plan
    goal = db.query(Goal).filter(Goal.id == progress_data.goal_id).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    
    # Extract original plan
    original_plan = goal.ai_generated_plan
    
    # Apply adaptation logic
    adapted_plan = adapt_plan_based_on_progress(original_plan, progress_data)
    
    # Update the goal with the adapted plan
    goal.ai_generated_plan = adapted_plan
    db.commit()
    
    return AdaptedPlan(
        tasks=adapted_plan.get("tasks", []),
        adaptations=adapted_plan.get("adaptations", [])
    )

def adapt_plan_based_on_progress(
    original_plan: Dict[str, Any],
    progress_data: ProgressData
) -> Dict[str, Any]:
    """Adapt the plan based on user progress data"""
    adapted_plan = original_plan.copy()
    
    # Record this adaptation
    if "adaptations" not in adapted_plan:
        adapted_plan["adaptations"] = []
    
    adaptation = {
        "timestamp": datetime.now().isoformat(),
        "reason": "Progress update",
        "changes": []
    }
    
    # Check completion rate
    if progress_data.completion_rate < 0.6:
        # User is struggling, adjust difficulty
        for task in adapted_plan.get("tasks", []):
            if task.get("status") != "completed":
                original_difficulty = task.get("difficulty", 5)
                task["difficulty"] = max(1, original_difficulty - 1)
                task["estimatedTimeMinutes"] = int(task.get("estimatedTimeMinutes", 60) * 1.2)
                
                adaptation["changes"].append({
                    "task_id": task.get("id"),
                    "field": "difficulty",
                    "old_value": original_difficulty,
                    "new_value": task["difficulty"],
                    "reason": "User struggling with pace"
                })
    
    # Additional adaptation logic...
    
    adapted_plan["adaptations"].append(adaptation)
    return adapted_plan
```

## UI/UX Implementation

### 1. Goal Creation and Assessment Flow

React components for goal creation:

```jsx
// src/components/GoalCreation/GoalForm.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { aiService } from '../../services/aiService';
import { goalService } from '../../services/goalService';

const GoalForm = () => {
  const [goal, setGoal] = useState('');
  const [domain, setDomain] = useState('');
  const [availableTime, setAvailableTime] = useState(60); // Default 60 minutes per day
  const [isProcessing, setIsProcessing] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsProcessing(true);
    setError('');
    
    try {
      // Step 1: Analyze the goal with AI
      const analysisResult = await aiService.analyzeGoal({
        user_goal: goal,
        domain,
        available_time_per_day: availableTime
      });
      
      // Step 2: Save the goal with the AI-generated plan
      const savedGoal = await goalService.createGoal({
        title: goal,
        domain_id: domain,
        ai_generated_plan: analysisResult
      });
      
      // Redirect to the assessment page
      navigate(`/goals/${savedGoal.id}/assessment`);
    } catch (error) {
      setError('Failed to process goal. Please try again.');
      console.error(error);
    } finally {
      setIsProcessing(false);
    }
  };
  
  return (
    <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl p-6">
      <h2 className="text-2xl font-bold mb-4">Create Your Solo Leveling Goal</h2>
      
      {error && <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">{error}</div>}
      
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="goal">
            What goal do you want to achieve?
          </label>
          <textarea
            id="goal"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
            placeholder="e.g., I want to become proficient in React development"
            rows="3"
            required
          />
        </div>
        
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="domain">
            Domain
          </label>
          <select
            id="domain"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
            required
          >
            <option value="">Select a domain</option>
            <option value="1">React Development</option>
            <option value="2">Python Programming</option>
            <option value="3">Fitness</option>
            <option value="4">Language Learning</option>
            <option value="5">Other</option>
          </select>
        </div>
        
        <div className="mb-6">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="availableTime">
            How much time can you dedicate per day? (minutes)
          </label>
          <input
            id="availableTime"
            type="number"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            value={availableTime}
            onChange={(e) => setAvailableTime(parseInt(e.target.value) || 0)}
            min="15"
            max="480"
            required
          />
        </div>
        
        <div className="flex items-center justify-between">
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
            disabled={isProcessing}
          >
            {isProcessing ? 'Processing...' : 'Create Goal'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default GoalForm;
```

### 2. Dashboard Implementation

React dashboard component:

```jsx
// src/components/Dashboard/DashboardView.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { dashboardService } from '../../services/dashboardService';
import { taskService } from '../../services/taskService';

import RankBadge from './RankBadge';
import TaskList from './TaskList';
import ProgressBar from './ProgressBar';
import MilestoneTracker from './MilestoneTracker';

const DashboardView = () => {
  const { id: userId } = useParams();
  const [dashboardData, setDashboardData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState('');
  
  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const data = await dashboardService.getUserDashboar
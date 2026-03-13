---
name: api-designer
description: RESTful API design with validation and error handling. Use when you need to design API endpoints, create API documentation, or when the user asks to "design API", "create endpoints", or "build API". Follows API design principles and best practices.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch, mcp__ide__getDiagnostics
hooks:
  before:
    - echo "🔌 Starting API design process..."
  after:
    - echo "✅ API design complete. Ready for implementation."
---

# /api - RESTful API Design & Implementation

## What This Skill Does
Designs and implements RESTful APIs with comprehensive validation, error handling, and documentation. Follows industry best practices for API design, security, and maintainability.

## When to Use This Skill
- Designing new API endpoints
- Creating API documentation
- Implementing CRUD operations
- When user says "design API", "create endpoints", "build API"
- Need API validation and error handling
- Setting up API architecture

## Core Process

### Step 1: API Design Phase
**Objective**: Design clear, consistent API architecture

1. **Resource Identification**
   - Identify core resources
   - Define resource relationships
   - Plan resource hierarchy
   - Consider RESTful principles

2. **Endpoint Design**
   - Define CRUD operations
   - Choose HTTP methods appropriately
   - Design URL patterns
   - Plan query parameters

3. **Request/Response Design**
   - Define request payloads
   - Design response formats
   - Plan status codes
   - Consider pagination

4. **Authentication & Security**
   - Choose authentication method
   - Define security requirements
   - Plan rate limiting
   - Consider input validation

### Step 2: Implementation Phase
**Objective**: Implement robust API endpoints

5. **Project Structure Setup**
   - Organize API code structure
   - Set up routing system
   - Configure middleware
   - Define controller patterns

6. **Validation Implementation**
   - Implement input validation
   - Define validation rules
   - Create custom validators
   - Handle validation errors

7. **Error Handling**
   - Define error response format
   - Implement global error handler
   - Create custom error classes
   - Handle expected and unexpected errors

8. **Middleware Setup**
   - Configure authentication middleware
   - Add logging middleware
   - Implement rate limiting
   - Set up CORS policies

### Step 3: Documentation & Testing
**Objective**: Create documentation and verify implementation

9. **API Documentation**
   - Write OpenAPI/Swagger specs
   - Document endpoints and parameters
   - Provide examples for requests/responses
   - Include error documentation

10. **Testing Implementation**
   - Write unit tests for controllers
   - Create integration tests
   - Test validation and error scenarios
   - Add performance tests

11. **Performance Optimization**
   - Implement caching strategies
   - Optimize database queries
   - Add pagination for large datasets
   - Consider compression

12. **Monitoring Setup**
   - Add request logging
   - Set up performance monitoring
   - Configure error tracking
   - Establish alerts

## Có phối hợp

### Inputs
- Data models or database schema
- Resource definitions and requirements
- Authentication method preferences
- Performance requirements
- Documentation needs

### Outputs
```markdown
## API Design & Implementation

### API Overview
**Base URL**: /api/v1
**Authentication**: JWT Bearer token
**Content Type**: application/json
**Rate Limit**: 100 requests/minute

### Resources & Endpoints
#### Users Resource
- `GET /api/v1/users` - List users (with pagination)
- `POST /api/v1/users` - Create new user
- `GET /api/v1/users/{id}` - Get user by ID
- `PATCH /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

### Request/Response Examples
**Create User Request**:
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securePassword123"
}
```

**Response Format**:
```json
{
  "data": { ...resource },
  "meta": {
    "page": 1,
    "total": 100
  }
}
```

### Error Handling
**Standard Error Response**:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [...field errors...]
  }
}
```

### Validation Rules
- Email: Valid email format
- Password: Minimum 8 chars, 1 uppercase, 1 number
- Name: Required, 2-50 characters

Ready for implementation.
```

## Key Principles

### 1. RESTful Architecture
- Use appropriate HTTP methods
- Follow RESTful naming conventions
- Stateless design
- Resource-based URLs

### 2. Consistent Naming
- Use kebab-case for URLs
- Use camelCase for JSON properties
- Plural nouns for resources
- Clear, descriptive names

### 3. Comprehensive Validation
- Validate all inputs
- Provide clear error messages
- Handle edge cases
- Protect against injection attacks

### 4. Proper Error Handling
- Use appropriate HTTP status codes
- Consistent error response format
- Provide actionable error messages
- Log errors for debugging

## Success Metrics
- **API Consistency**: All endpoints follow same conventions
- **Documentation Quality**: Complete, accurate API docs
- **Validation Coverage**: All inputs validated
- **Error Handling**: Comprehensive error scenarios covered
- **Testing Coverage**: High test coverage for API endpoints
- **Performance**: Fast response times, proper pagination

## Common Pitfalls to Avoid
- **Inconsistent Naming**: Mixed naming conventions
- **Missing Validation**: No input validation
- **Poor Error Messages**: Unhelpful error responses
- **Over-Engineering**: Too complex for requirements
- **Missing Documentation**: No or inaccurate docs
- **Security Issues**: Missing authentication/authorization

## Tips for Effective API Design

### 1. Follow Standard Conventions
- Use standard HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Use appropriate status codes (200, 201, 400, 401, 403, 404, 500)
- Plurals for resources (/users, not /user)
- Nouns not verbs in URLs

### 2. Design for Consumers
- Make APIs intuitive and easy to use
- Provide clear, consistent responses
- Document all parameters and responses
- Version APIs appropriately

### 3. Security First
- Always validate inputs
- Implement authentication
- Use HTTPS
- Implement rate limiting
- Sanitize outputs

### 4. Performance Considerations
- Implement pagination for large datasets
- Add appropriate caching headers
- Optimize database queries
- Consider compression

## API Design Patterns

### 1. CRUD Pattern
- Create: POST /resource
- Read: GET /resource, GET /resource/{id}
- Update: PUT /resource/{id}, PATCH /resource/{id}
- Delete: DELETE /resource/{id}

### 2. Search & Filtering
- GET /resource?filter=value&search=query&sort=field
- Use query parameters for filters
- Support pagination with page/size or cursor
- Allow sorting on multiple fields

### 3. Relationships
- Nested resources: GET /resource/{id}/subresource
- Use IDs for references
- Include options embedding related resources
- Document relationship operations

### 4. Batch Operations
- POST /resource/batch with array of operations
- Support bulk create/update/delete
- Return batch results with per-item status
- Handle partial failures gracefully

## Validation Strategy

### 1. Input Validation Rules
- Required fields enforcement
- Type checking (string, number, boolean, array, object)
- Length constraints (min/max)
- Format validation (email, URL, date)
- Custom validation rules

### 2. Validation Libraries
- Zod: Type-safe schema validation
- Joi: Rich validation library
- Yup: Schema validation
- Custom validators as needed

### 3. Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

## Error Handling Strategy

### 1. HTTP Status Codes
- 200: Success
- 201: Created
- 400: Bad Request (validation errors)
- 401: Unauthorized (missing/invalid auth)
- 403: Forbidden (insufficient permissions)
- 404: Not Found
- 409: Conflict (resource already exists)
- 422: Unprocessable Entity (business logic error)
- 429: Too Many Requests (rate limit)
- 500: Internal Server Error

### 2. Error Response Format
- Consistent structure across all endpoints
- Error codes for programmatic handling
- Human-readable messages
- Optional additional details

### 3. Global Error Handler
- Catch all unhandled errors
- Log errors with context
- Return appropriate responses
- Send alerts for server errors

## Security Implementation

### 1. Authentication
- JWT with refresh tokens
- Session-based auth
- API key for service-to-service
- OAuth 2.0 for third-party integration

### 2. Authorization
- Role-based access control (RBAC)
- Permission-based access control (PBAC)
- Resource ownership validation
- Scope-based restrictions

### 3. Input Sanitization
- SQL injection prevention
- XSS prevention
- Command injection prevention
- File upload restrictions
- Rate limiting to prevent abuse

## Testing Strategy

### 1. Unit Tests
- Test controller functions
- Validate request/response logic
- Test error handling
- Test authentication/authorization

### 2. Integration Tests
- Test API endpoints with database
- Test external service integration
- Test authentication flows
- Test error scenarios

### 3. Performance Tests
- Load testing for endpoints
- Stress testing for scalability
- Response time testing
- Concurrent request testing

## Documentation Essentials

### 1. OpenAPI Specification
- Define all API endpoints
- Document request/response schemas
- Include examples
- Describe authentication

### 2. README Documentation
- API overview and purpose
- Getting started guide
- Authentication instructions
- Error code reference
- Rate limiting information

### 3. Changelog
- Track API changes
- Document breaking changes
- Version API appropriately
- Maintain backward compatibility

## Best Practices
- Design APIs for longevity, not just current needs
- Use consistent naming conventions throughout
- Validate inputs rigorously and provide clear errors
- Version APIs when making breaking changes
- Document everything for API consumers
- Implement proper authentication and authorization
- Monitor API usage and performance
- Write comprehensive tests
- Consider rate limiting from the start
- Provide detailed error messages for debugging
- Plan for scalability and performance
- Follow security best practices always
- Use appropriate HTTP status codes
- Support pagination for large datasets
- Implement proper logging for debugging

## Example Workflow
```
Input: "Create user management API"

Process:
1. Design Phase:
   - Resources: users, roles, permissions
   - Endpoints: CRUD for each resource
   - Authentication: JWT-based
   - Authorization: RBAC

2. Implementation:
   - Project structure: Controllers, services, routes, middleware
   - Validation: Zod schemas for all inputs
   - Error handling: Global error handler with consistent format
   - Security: Authentication middleware, RBAC

3. Documentation:
   - OpenAPI spec with all endpoints
   - Examples for each operation
   - Error code reference
   - Authentication guide

4. Testing:
   - Unit tests: 100% coverage of controllers
   - Integration tests: All endpoints with database
   - Performance: Load testing with 1000 concurrent users

5. Deployment:
   - API deployed to /api/v1
   - Documentation available at /api/docs
   - Monitoring: Dashboard with key metrics
   - Alerts: Set up for error rate > 1%
```

## Output Quality Checklist
- [ ] RESTful principles followed
- [ ] Consistent naming conventions
- [ ] Comprehensive validation implemented
- [ ] Proper error handling with consistent format
- [ ] Authentication and authorization secured
- [ ] Complete API documentation
- [ ] Comprehensive test coverage
- [ ] Performance optimizations applied
- [ ] Security best practices implemented
- [ ] Monitoring and logging configured
---
name: deployer
description: Cloud deployment with rollback strategy. Use when you need to deploy applications, manage releases, or when the user asks to "deploy", "release to production", or "push to cloud". Implements safe deployment with rollback capabilities.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch, mcp__ide__getDiagnostics
hooks:
  before:
    - echo "🚀 Starting deployment process..."
  after:
    - echo "✅ Deployment complete. Monitoring active."
---

# /deploy - Cloud Deployment with Rollback Strategy

## What This Skill Does
Implements safe, reliable cloud deployments with comprehensive rollback strategies. Covers build optimization, deployment to various cloud platforms, monitoring, and rollback procedures for production environments.

## When to Use This Skill
- Ready to release to production
- Deploying new features or updates
- Managing application releases
- When user says "deploy", "release to production", "push to cloud"
- Need safe deployment with rollback capabilities
- Want monitoring and alerting setup

## Core Process

### Step 1: Pre-Deployment Preparation
**Objective**: Ensure readiness for deployment

1. **Verification Check**
   - Run final verification tests
   - Check build success
   - Verify all quality gates passed
   - Confirm no blocking issues

2. **Environment Preparation**
   - Prepare deployment environment
   - Check infrastructure status
   - Verify database connections
   - Ensure external services ready

3. **Rollback Planning**
   - Identify rollback triggers
   - Prepare rollback procedures
   - Create backup plans
   - Document rollback steps

4. **Deployment Strategy**
   - Choose deployment method (blue-green, canary, etc.)
   - Plan traffic routing
   - Schedule maintenance windows
   - Notify stakeholders

### Step 2: Build Optimization
**Objective**: Create optimized deployment artifacts

1. **Build Process**
   - Run production build
   - Optimize bundle sizes
   - Minify and compress assets
   - Generate source maps

2. **Security Hardening**
   - Remove development dependencies
   - Apply security patches
   - Configure security headers
   - Set up content security policies

3. **Performance Optimization**
   - Implement code splitting
   - Optimize images and assets
   - Set up caching strategies
   - Configure CDN if applicable

4. **Configuration Management**
   - Prepare environment variables
   - Set up configuration files
   - Create deployment manifests
   - Prepare secrets management

### Step 3: Deployment Execution
**Objective**: Deploy application to target environment

1. **Deployment Method Selection**
   - Choose appropriate deployment strategy
   - Configure deployment tools
   - Set up deployment scripts
   - Prepare deployment pipeline

2. **Application Deployment**
   - Deploy application code
   - Configure services and databases
   - Set up environment variables
   - Verify deployment success

3. **Database Migration**
   - Apply database schema changes
   - Run data migrations
   - Verify data integrity
   - Create backups before migration

4. **Service Configuration**
   - Configure load balancers
   - Set up health checks
   - Configure monitoring
   - Establish logging

### Step 4: Post-Deployment Verification
**Objective**: Confirm deployment success and monitor

1. **Health Checks**
   - Verify application health
   - Test critical functionality
   - Check API endpoints
   - Monitor system metrics

2. **Performance Monitoring**
   - Track response times
   - Monitor resource usage
   - Check error rates
   - Verify scalability

3. **User Experience Monitoring**
   - Track user interactions
   - Monitor conversion rates
   - Check for usability issues
   - Gather user feedback

4. **Rollback Monitoring**
   - Monitor for rollback triggers
   - Set up alerting
   - Track deployment metrics
   - Document deployment status

## Có phối hợp

### Inputs
- Application code and configuration
- Deployment target and platform
- Build artifacts and dependencies
- Environment variables and secrets
- Monitoring and alerting setup

### Outputs
```markdown
## Deployment Report

### Pre-Deployment
**Verification Status**: [Passed/Failed]
**Build Status**: [Success/Issues]
**Rollback Plan**: [Strategy and procedures]

### Deployment Execution
**Deployment Method**: [Strategy used]
**Target Environment**: [Platform and location]
**Deployment Time**: [Duration]
**Success Status**: [Success/Partial/Failed]

### Post-Deployment
**Health Checks**: [Results]
**Performance Metrics**: [Key indicators]
**User Experience**: [Monitoring results]
**Rollback Readiness**: [Status]

### Monitoring Setup
**Alerting**: [Configured alerts]
**Logging**: [Logging setup]
**Metrics**: [Key metrics tracked]
**Rollback Triggers**: [Defined triggers]

Ready for monitoring.
```

## Key Features

### 1. Safe Deployment Strategies
- Blue-green deployments
- Canary releases
- Rolling updates
- Feature flags
- Zero-downtime deployments

### 2. Comprehensive Rollback
- Automatic rollback triggers
- Manual rollback procedures
- Database rollback strategies
- Configuration rollback
- Traffic routing rollback

### 3. Multi-Platform Support
- Vercel/Netlify for static sites
- AWS for cloud infrastructure
- Docker for containerization
- Kubernetes for orchestration
- Custom deployment pipelines

### 4. Monitoring and Alerting
- Health checks and monitoring
- Performance metrics tracking
- Error rate monitoring
- User experience tracking
- Automated alerting

## Success Metrics
- **Deployment Success Rate**: Percentage of successful deployments
- **Rollback Frequency**: How often rollbacks occur
- **Deployment Time**: Average deployment duration
- **Mean Time to Recovery**: Time to restore service
- **User Impact**: Minimal user disruption

## Common Deployment Scenarios

### Scenario 1: Static Site Deployment
```
Input: "Deploy React app to Vercel"
Process:
1. Build Optimization: Create optimized static build
2. Pre-Deployment: Verify build and run tests
3. Deployment: Deploy to Vercel with preview URLs
4. Verification: Check health and performance
5. Monitoring: Set up Vercel analytics
6. Rollback: Use Vercel rollback if needed
```

### Scenario 2: Node.js API Deployment
```
Input: "Deploy Node.js API to AWS"
Process:
1. Build Optimization: Create Docker image with optimizations
2. Pre-Deployment: Verify migrations and health checks
3. Deployment: Deploy to ECS or Lambda with blue-green
4. Verification: Test API endpoints and performance
5. Monitoring: Set up CloudWatch and alarms
6. Rollback: Use CloudFormation rollback
```

### Scenario 3: Database Migration Deployment
```
Input: "Deploy with database migration"
Process:
1. Build Optimization: Create migration scripts
2. Pre-Deployment: Backup database, test migrations
3. Deployment: Deploy code, run migrations
4. Verification: Check data integrity, test functionality
5. Monitoring: Monitor database performance
6. Rollback: Plan for data rollback if needed
```

## Output Quality Checklist
- [ ] Build successfully optimized
- [ ] All tests passed
- [ ] Rollback plan prepared
- [ ] Deployment executed successfully
- [ ] Health checks passed
- [ ] Monitoring configured
- [ ] Rollback triggers set up
- [ ] Documentation updated
- [ ] Stakeholders notified

## Integration with Other Skills
- **Tester**: Ensures tests pass before deployment
- **Verifier**: Provides verification evidence
- **Fixer**: Resolves issues found during deployment
- **Debugger**: Handles deployment-related errors
- **UI Designer**: Ensures design quality in deployment

## Advanced Deployment Features

### 1. Feature Flags
- Gradual feature rollout
- A/B testing capabilities
- Quick feature disable
- User segmentation
- Performance monitoring

### 2. Progressive Delivery
- Canary deployments
- Traffic splitting
- Gradual traffic increase
- Automated rollback
- Performance monitoring

### 3. Infrastructure as Code
- Terraform for infrastructure
- CloudFormation for AWS
- Docker for containerization
- Kubernetes for orchestration
- Automated provisioning

### 4. Security Hardening
- Security scanning
- Dependency vulnerability checks
- Configuration security
- Access control
- Secrets management

## Deployment Strategies

### 1. Blue-Green Deployment
- Two identical production environments
- Zero downtime switching
- Instant rollback capability
- Traffic routing control
- Health check verification

### 2. Canary Deployment
- Gradual traffic increase
- Risk reduction
- Performance monitoring
- Automated rollback
- User feedback collection

### 3. Rolling Update
- Gradual instance replacement
- No downtime
- Load balancing
- Health check verification
- Controlled rollout

### 4. Feature Flag Deployment
- Code deployed but features disabled
- Gradual feature enablement
- Quick disable capability
- A/B testing support
- User segmentation

## Rollback Triggers

### 1. Automated Triggers
- High error rates
- Performance degradation
- Health check failures
- User experience metrics
- Security alerts

### 2. Manual Triggers
- Stakeholder requests
- Business decisions
- User feedback
- Performance issues
- Feature problems

### 3. Time-Based Triggers
- Maintenance windows
- Scheduled rollbacks
- Time-based feature flags
- Automated cleanup
- Resource management

## Monitoring and Alerting

### 1. Health Monitoring
- Application health checks
- Service availability
- Database connectivity
- External service status
- System metrics

### 2. Performance Monitoring
- Response times
- Error rates
- Throughput
- Resource usage
- Scalability metrics

### 3. User Experience Monitoring
- User interactions
- Conversion rates
- Page load times
- Mobile performance
- Accessibility

### 4. Security Monitoring
- Security events
- Access logs
- Vulnerability scans
- Anomaly detection
- Compliance checks

## Best Practices
- Always verify before deploying
- Have rollback plan ready
- Use feature flags for new features
- Monitor everything in production
- Automate where possible
- Document everything
- Learn from each deployment
- Keep stakeholders informed
- Plan for maintenance windows
- Consider user impact
- Test in production-like environments
- Have disaster recovery plans
- Use infrastructure as code
- Implement security best practices
- Monitor performance continuously
- Gather user feedback
- Iterate based on data
- Keep deployment times short
- Minimize downtime
- Ensure data integrity
- Plan for scalability
- Consider cost optimization
- Maintain documentation
- Train team members
- Have clear communication channels
- Define success criteria
- Plan for edge cases
- Consider compliance requirements
- Implement backup strategies
- Test rollback procedures
- Monitor post-deployment
- Have incident response plans
- Keep improving processes
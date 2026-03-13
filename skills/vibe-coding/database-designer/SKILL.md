---
name: database-designer
description: Database schema design and optimization. Use when you need to design database schemas, create ERD diagrams, or when the user asks to "design database", "create schema", or "plan database". Covers schema design, indexing, migrations, and optimization.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch, mcp__ide__getDiagnostics
hooks:
  before:
    - echo "🗄️ Starting database design process..."
  after:
    - echo "✅ Database design complete. Ready for implementation."
---

# /erd - Database Schema Design & ERD Creation

## What This Skill Does
Designs comprehensive database schemas with ERD diagrams, indexing strategies, and optimization plans. Covers schema design, data modeling, migration planning, and performance optimization for various database systems.

## When to Use This Skill
- Designing new database schemas
- Creating ERD diagrams for documentation
- Planning database migrations
- When user says "design database", "create schema", "plan database"
- Need database optimization strategies
- Setting up data models for applications

## Core Process

### Step 1: Requirements Analysis
**Objective**: Understand data needs and constraints

1. **Entity Identification**
   - Identify main entities (tables)
   - Define entity relationships
   - Consider business rules
   - Understand data lifecycle

2. **Data Modeling**
   - Choose appropriate data types
   - Define field constraints
   - Plan for data validation
   - Consider data growth

3. **Relationship Mapping**
   - Identify one-to-one relationships
   - Map one-to-many relationships
   - Define many-to-many relationships
   - Plan for foreign key constraints

4. **Normalization Analysis**
   - Apply 1st normal form (1NF)
   - Apply 2nd normal form (2NF)
   - Apply 3rd normal form (3NF)
   - Consider denormalization trade-offs

### Step 2: Schema Design
**Objective**: Create optimized database structure

5. **Table Design**
   - Define primary keys
   - Choose appropriate data types
   - Plan for indexing
   - Consider partitioning

6. **Index Strategy**
   - Identify query patterns
   - Plan composite indexes
   - Consider unique constraints
   - Plan for performance optimization

7. **Constraint Implementation**
   - Define foreign key constraints
   - Add check constraints
   - Plan for cascading actions
   - Consider business rules

8. **Performance Planning**
   - Plan for query optimization
   - Consider denormalization
   - Plan for caching strategies
   - Design for scalability

### Step 3: Migration Planning
**Objective**: Plan safe database changes

9. **Migration Strategy**
   - Plan for schema evolution
   - Define migration order
   - Consider data migration
   - Plan for rollback

10. **Data Migration**
    - Plan data transformation
    - Consider data validation
    - Plan for data seeding
    - Consider data backup

11. **Rollback Planning**
    - Define rollback procedures
    - Plan for data recovery
    - Consider point-in-time recovery
    - Plan for disaster recovery

12. **Testing Strategy**
    - Plan for schema testing
    - Consider data validation tests
    - Plan for performance testing
    - Define testing environments

## Có phối hợp

### Inputs
- Application requirements and features
- Data models and relationships
- Performance requirements
- Technology stack preferences
- Migration needs

### Outputs
```markdown
## Database Schema Design

### Schema Overview
**Database Type**: PostgreSQL/MySQL/SQLite
**Version**: Latest stable
**Authentication**: PostgreSQL authentication
**Connection Pooling**: Enabled with 20 connections

### Entity-Relationship Diagram
**Entities**:
- Users (id, email, name, created_at, updated_at)
- Roles (id, name, permissions, created_at)
- UserRoles (user_id, role_id, assigned_at)

**Relationships**:
- Users:Roles = Many-to-Many
- Users:Posts = One-to-Many
- Posts:Comments = One-to-Many

### Table Definitions
**Users Table**:
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  deleted_at TIMESTAMP,
  CONSTRAINT users_email_check CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$')
);
```

### Index Strategy
**Primary Indexes**:
- Users: id (primary key)
- Users: email (unique)

**Secondary Indexes**:
- Users: created_at (for recent queries)
- Users: deleted_at (for soft deletes)

### Migration Plan
**Phase 1**: Initial schema creation
**Phase 2**: Data seeding
**Phase 3**: Performance optimization
**Phase 4**: Backup and verification

Ready for Prisma implementation.
```

## Key Principles

### 1. Data Modeling Best Practices
- Choose appropriate data types
- Use meaningful naming conventions
- Plan for data growth
- Consider future requirements

### 2. Performance Optimization
- Index wisely based on query patterns
- Avoid over-indexing
- Consider denormalization trade-offs
- Plan for query optimization

### 3. Data Integrity
- Use appropriate constraints
- Plan for cascading actions
- Consider business rules
- Implement proper validation

### 4. Scalability Planning
- Design for horizontal scaling
- Consider partitioning strategies
- Plan for sharding if needed
- Design for high availability

## Success Metrics
- **Schema Quality**: Normalized, optimized design
- **Performance**: Query times meet requirements
- **Integrity**: Data constraints properly enforced
- **Scalability**: Design supports growth
- **Maintainability**: Schema is clear and well-documented

## Common Pitfalls to Avoid
- **Over-Normalization**: Too many joins, performance issues
- **Missing Indexes**: Slow queries due to lack of indexes
- **Inconsistent Naming**: Mixed naming conventions
- **Poor Data Types**: Inefficient storage, performance issues
- **Missing Constraints**: Data integrity problems
- **No Migration Plan**: Schema changes break production

## Tips for Effective Database Design

### 1. Start with Business Requirements
- Understand what data needs to be stored
- Identify key entities and relationships
- Consider business rules and constraints
- Plan for reporting and analytics needs

### 2. Choose the Right Database System
- Consider data structure and access patterns
- Evaluate scalability requirements
- Consider team expertise
- Factor in cost and licensing

### 3. Design for Performance
- Index based on query patterns
- Use appropriate data types
- Consider denormalization for read-heavy workloads
- Plan for caching strategies

### 4. Plan for Evolution
- Design for schema changes
- Plan migration strategies
- Consider backward compatibility
- Document design decisions

## Database Design Patterns

### 1. User Management Pattern
```sql
-- Users table with soft deletes and timestamps
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  deleted_at TIMESTAMP
);

-- User roles for RBAC
CREATE TABLE roles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) UNIQUE NOT NULL,
  permissions JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- User-role junction table
CREATE TABLE user_roles (
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  role_id UUID REFERENCES roles(id) ON DELETE CASCADE,
  assigned_at TIMESTAMP DEFAULT NOW(),
  PRIMARY KEY (user_id, role_id)
);
```

### 2. Content Management Pattern
```sql
-- Content with versioning
CREATE TABLE content (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title VARCHAR(500) NOT NULL,
  body TEXT NOT NULL,
  status VARCHAR(50) DEFAULT 'draft',
  author_id UUID REFERENCES users(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  published_at TIMESTAMP,
  version INTEGER DEFAULT 1
);

-- Content history for audit trail
CREATE TABLE content_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_id UUID REFERENCES content(id) ON DELETE CASCADE,
  title VARCHAR(500),
  body TEXT,
  version INTEGER NOT NULL,
  changed_at TIMESTAMP DEFAULT NOW(),
  changed_by UUID REFERENCES users(id)
);
```

### 3. E-commerce Pattern
```sql
-- Products with categories
CREATE TABLE categories (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  parent_id UUID REFERENCES categories(id)
);

-- Products with inventory
CREATE TABLE products (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(500) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  category_id UUID REFERENCES categories(id),
  stock_quantity INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Orders with order items
CREATE TABLE orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  status VARCHAR(50) DEFAULT 'pending',
  total_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE order_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id UUID REFERENCES orders(id) ON DELETE CASCADE,
  product_id UUID REFERENCES products(id),
  quantity INTEGER NOT NULL,
  price DECIMAL(10, 2) NOT NULL
);
```

## Index Strategy

### 1. Primary Indexes
- Always create primary key indexes
- Use appropriate data types for keys
- Consider UUID vs auto-increment
- Plan for composite keys if needed

### 2. Secondary Indexes
- Index foreign keys for joins
- Index frequently filtered columns
- Create composite indexes for common query patterns
- Consider partial indexes for specific conditions

### 3. Performance Indexes
- Index for sorting (ORDER BY columns)
- Index for filtering (WHERE clause columns)
- Index for joining (foreign key columns)
- Index for unique constraints

### 4. Index Maintenance
- Monitor index usage
- Remove unused indexes
- Rebuild fragmented indexes
- Consider index size and overhead

## Migration Planning

### 1. Migration Strategy
- Use migration tools (Prisma, Flyway, Liquibase)
- Plan migration order carefully
- Test migrations in staging
- Consider data migration needs

### 2. Data Migration
- Plan data transformation
- Consider data validation
- Plan for data seeding
- Consider data backup

### 3. Rollback Planning
- Define rollback procedures
- Plan for data recovery
- Consider point-in-time recovery
- Plan for disaster recovery

### 4. Testing Strategy
- Test schema changes in isolation
- Test with production-like data
- Consider performance testing
- Define testing environments

## Database Systems Support

### 1. PostgreSQL
- Advanced features (JSONB, arrays, hstore)
- Excellent for complex queries
- Strong ACID compliance
- Good for analytical workloads

### 2. MySQL
- Simple, fast for simple queries
- Good for web applications
- Excellent replication
- Good for simple data models

### 3. SQLite
- Embedded, serverless
- Good for mobile/desktop apps
- Simple to deploy
- Good for small applications

### 4. MongoDB
- Document-based
- Good for unstructured data
- Excellent for rapid development
- Good for content management

## Best Practices
- Always start with requirements, not technology
- Normalize data but consider denormalization trade-offs
- Index based on actual query patterns
- Use appropriate data types for storage efficiency
- Plan for schema evolution and migrations
- Consider security and access control
- Document everything thoroughly
- Test with realistic data volumes
- Monitor performance in production
- Plan for backup and disaster recovery
- Consider high availability requirements
- Use appropriate constraints for data integrity
- Design for the specific database system's strengths
- Consider the team's expertise and maintenance needs
- Factor in cost and licensing
- Plan for scalability from the start
- Consider compliance requirements
- Implement proper error handling
- Use transactions for data consistency
- Consider read replicas for read-heavy workloads
- Plan for connection pooling
- Consider partitioning for large tables
- Use appropriate character sets and collations
- Implement proper auditing and logging
- Consider GDPR and other privacy regulations
- Plan for data retention and archiving

## Example Workflow
```
Input: "Design database for task management app"

Process:
1. Requirements Analysis:
   - Entities: Users, Tasks, Categories, Comments
   - Relationships: Users have many tasks, tasks have many comments
   - Performance: Fast task listing, search

2. Schema Design:
   - Users: id, email, name, created_at, updated_at
   - Categories: id, name, parent_id
   - Tasks: id, title, description, status, priority, user_id, category_id
   - Comments: id, task_id, user_id, content, created_at

3. Index Strategy:
   - Users: id (primary), email (unique)
   - Tasks: id (primary), user_id, category_id, status, created_at
   - Comments: id (primary), task_id, created_at

4. Migration Plan:
   - Phase 1: Create all tables
   - Phase 2: Add indexes
   - Phase 3: Seed initial data
   - Phase 4: Performance optimization

5. Implementation:
   - Create Prisma schema
   - Generate migrations
   - Test with sample data
   - Verify query performance

6. Documentation:
   - ERD diagram
   - Schema documentation
   - Index strategy
   - Migration procedures
```

## Output Quality Checklist
- [ ] All entities and relationships identified
- [ ] Appropriate data types chosen
- [ ] Primary and secondary indexes planned
- [ ] Foreign key constraints defined
- [ ] Migration strategy documented
- [ ] Performance considerations addressed
- [ ] Rollback procedures defined
- [ ] Testing strategy planned
- [ ] Documentation complete
- [ ] Ready for Prisma implementation
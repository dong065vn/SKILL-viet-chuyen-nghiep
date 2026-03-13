---
name: ui-designer
description: UI/UX design intelligence with search engine. Use when you need to design user interfaces, create design systems, or when the user asks to "design UI", "create interface", or "build UI with specific style". Implements design intelligence with 50+ styles, 97 palettes, and 57 fonts.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, TaskCreate, TaskUpdate, TaskGet, TaskList, Bash, WebSearch, WebFetch, mcp__ide__getDiagnostics
hooks:
  before:
    - echo "🎨 Starting UI/UX design process..."
  after:
    - echo "✅ UI/UX design complete. Ready for implementation."
---

# /ui - UI/UX Pro Max Design Intelligence

## What This Skill Does
Provides intelligent UI/UX design with search engine capabilities, offering 50+ design styles, 97 color palettes, 57 fonts, and 9+ technology stacks. Creates comprehensive design systems, detailed specifications, and implementation-ready designs.

## When to Use This Skill
- Starting new UI projects
- Designing specific components or screens
- Creating design systems
- When user says "design UI", "create interface", "build UI"
- Need design intelligence with specific style requirements
- Want professional UI/UX with search engine capabilities

## Core Process

### Step 1: Design System Generation
**Objective**: Create foundational design system

1. **Style Selection**
   - Choose from 50+ design styles (modern, minimal, material, etc.)
   - Select color palette from 97 options
   - Pick typography from 57 font families
   - Choose technology stack (React, Vue, etc.)

2. **Design Principles**
   - Define visual hierarchy
   - Establish spacing and layout rules
   - Set color usage guidelines
   - Define typography scales

3. **Component Library**
   - Create reusable component patterns
   - Define interaction behaviors
   - Establish animation guidelines
   - Set accessibility standards

4. **Design Tokens**
   - Define colors, spacing, typography
   - Create CSS variables or theme objects
   - Establish design consistency
   - Plan for theming and dark mode

### Step 2: Detailed Design Search
**Objective**: Find and adapt specific design patterns

1. **Search Engine Queries**
   - Search for specific UI patterns
   - Find design inspiration
   - Locate component examples
   - Discover best practices

2. **Pattern Analysis**
   - Evaluate design effectiveness
   - Assess usability and accessibility
   - Consider technical feasibility
   - Adapt patterns to requirements

3. **Customization**
   - Modify patterns for specific needs
   - Adjust colors and typography
   - Adapt to brand guidelines
   - Ensure consistency with design system

4. **Documentation**
   - Document design decisions
   - Create usage guidelines
   - Provide implementation notes
   - Establish design rationale

### Step 3: Implementation Planning
**Objective**: Prepare for development

1. **Technical Specifications**
   - Define component APIs
   - Plan state management
   - Consider performance implications
   - Plan for responsiveness

2. **Development Strategy**
   - Break down into implementable tasks
   - Plan for progressive enhancement
   - Consider mobile-first approach
   - Plan for testing and validation

3. **Integration Planning**
   - Plan for existing codebase integration
   - Consider API requirements
   - Plan for data flow
   - Prepare for deployment

4. **Quality Assurance**
   - Define design consistency checks
   - Plan for accessibility testing
   - Consider cross-browser compatibility
   - Plan for performance optimization

## Có phối hợp

### Inputs
- Project description or requirements
- Target technology stack
- Design preferences or style requirements
- Brand guidelines or color schemes
- User needs and accessibility requirements

### Outputs
```markdown
## UI/UX Design System

### Design Overview
**Style**: [Selected style name]
**Color Palette**: [Primary colors and usage]
**Typography**: [Font families and scales]
**Technology Stack**: [React/Vue/Angular/etc.]

### Design Principles
**Visual Hierarchy**: [How elements are prioritized]
**Spacing Rules**: [Spacing scale and usage]
**Color Usage**: [When and how to use colors]
**Typography Guidelines**: [Font usage rules]

### Component Library
**Reusable Components**:
- [Component 1]: [Description and usage]
- [Component 2]: [Description and usage]

### Design Tokens
**Colors**:
- Primary: [Color value]
- Secondary: [Color value]
- Success: [Color value]
- Error: [Color value]

### Implementation Plan
**Technical Specifications**: [Component APIs and props]
**Development Strategy**: [Implementation approach]
**Quality Assurance**: [Testing and validation plan]

Ready for /css implementation.
```

## Key Features

### 1. Intelligent Design Search
- Access to 50+ design styles
- 97 color palettes to choose from
- 57 font families for typography
- 9+ technology stack support
- Pattern-based design suggestions

### 2. Design System Creation
- Complete design system generation
- Consistent design tokens
- Reusable component library
- Accessibility-first approach
- Responsive design planning

### 3. Implementation-Ready Designs
- Detailed technical specifications
- Component API definitions
- Performance considerations
- Testing strategies
- Deployment planning

### 4. Professional Quality
- Industry best practices
- Accessibility compliance
- Cross-browser compatibility
- Performance optimization
- Maintainable code structure

## Success Metrics
- **Design Quality**: Professional, consistent design
- **Implementation Readiness**: Clear specifications for developers
- **Accessibility**: WCAG compliance
- **Performance**: Optimized for speed and efficiency
- **User Satisfaction**: Meets user needs and expectations

## Common Design Scenarios

### Scenario 1: Modern Dashboard Design
```
Input: "Design a modern dashboard for analytics app"
Process:
1. Style Selection: Modern minimal with blue/white palette
2. Design System: Create dashboard-specific components
3. Search: Find dashboard patterns and best practices
4. Customization: Adapt to analytics requirements
5. Implementation: Plan React components with Chart.js integration
6. Quality: Ensure accessibility and responsiveness
```

### Scenario 2: E-commerce Product Page
```
Input: "Design e-commerce product page with mobile-first"
Process:
1. Style Selection: Clean, conversion-focused design
2. Design System: Product card, cart, checkout components
3. Search: Find e-commerce UX patterns and best practices
4. Customization: Adapt to brand and product requirements
5. Implementation: Plan responsive React components
6. Quality: Ensure mobile usability and fast loading
```

### Scenario 3: Mobile App Design
```
Input: "Design mobile banking app with dark mode"
Process:
1. Style Selection: Modern, secure-feeling design
2. Design System: Mobile-specific components and patterns
3. Search: Find mobile banking UX and security patterns
4. Customization: Adapt to banking requirements and regulations
5. Implementation: Plan React Native components
6. Quality: Ensure accessibility and security compliance
```

## Output Quality Checklist
- [ ] Design style clearly defined
- [ ] Color palette selected and documented
- [ ] Typography system established
- [ ] Component library created
- [ ] Design tokens defined
- [ ] Implementation plan provided
- [ ] Accessibility considerations included
- [ ] Responsive design planned
- [ ] Performance considerations addressed

## Integration with Other Skills
- **CSS Specialist**: Takes design system for implementation
- **Coder**: Provides design specifications for development
- **Tester**: Defines UI testing requirements
- **Verifier**: Uses design system for verification
- **Deployer**: Ensures design quality in deployment

## Advanced Design Features

### 1. Dark Mode Support
- Automatic dark/light theme switching
- Color system for both themes
- Component-level theme adaptation
- User preference detection

### 2. Responsive Design
- Mobile-first approach
- Breakpoint system
- Adaptive layouts
- Touch-friendly interactions

### 3. Accessibility Compliance
- WCAG 2.1 AA standards
- Screen reader support
- Keyboard navigation
- High contrast options
- Focus management

### 4. Performance Optimization
- Lazy loading for components
- Image optimization
- CSS-in-JS performance
- Bundle size considerations
- Runtime performance

## Design System Components

### Layout Components
- Grid systems
- Container components
- Spacing utilities
- Responsive breakpoints

### Navigation Components
- Navigation bars
- Sidebars
- Breadcrumbs
- Pagination

### Form Components
- Input fields
- Validation states
- Form layouts
- Error handling

### Data Display Components
- Tables
- Cards
- Lists
- Charts and graphs

### Interactive Components
- Modals
- Dropdowns
- Accordions
- Tabs

## Implementation Guidelines

### 1. Component Structure
```javascript
// Example component structure
const Button = ({
  variant = 'primary',
  size = 'medium',
  children,
  onClick,
  disabled,
  loading,
  className,
  ...props
}) => {
  // Component logic
};

Button.propTypes = {
  variant: PropTypes.oneOf(['primary', 'secondary', 'danger', 'success']),
  size: PropTypes.oneOf(['small', 'medium', 'large']),
  // ... other prop types
};
```

### 2. Styling Approach
- CSS-in-JS for component-level styles
- Design tokens for consistency
- Responsive design with breakpoints
- Theme switching for dark mode
- Performance-optimized CSS

### 3. State Management
- Local state for UI interactions
- Context for theme switching
- Props for component configuration
- Redux/Zustand for global state
- Form state management

## Quality Assurance

### 1. Design Consistency Checks
- Verify component usage consistency
- Check spacing and alignment
- Validate color usage
- Ensure typography consistency

### 2. Accessibility Testing
- Screen reader compatibility
- Keyboard navigation
- Color contrast verification
- Focus management testing

### 3. Cross-Browser Compatibility
- Test on major browsers
- Check for inconsistencies
- Validate CSS support
- Ensure feature detection

### 4. Performance Testing
- Measure load times
- Check bundle sizes
- Profile runtime performance
- Test on various devices

## Best Practices
- Always start with design system
- Consider accessibility from the start
- Plan for responsive design
- Think about performance implications
- Document design decisions
- Test with real users when possible
- Iterate based on feedback
- Keep design consistent across components
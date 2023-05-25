describe('Scenario Two', () => {
    beforeEach(() => {
    cy.visit('https://www.saucedemo.com/')
    })
    
    it('should log in with valid credentials', () => {
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.url().should('include', 'inventory.html')
    })
    
    it('should display error message for invalid credentials', () => {
    cy.get('#user-name').type('invalid_user')
    cy.get('#password').type('invalid_password')
    cy.get('#login-button').click()
    cy.url().should('not.include', 'inventory.html')
    })
    
    it('should display error message for empty username', () => {
    cy.get('#user-name').clear()
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.contains('Epic sadface: Username is required').should('be.visible')
    })
    
    it('should display error message for empty password', () => {
    cy.get('#user-name').type('standard_user')
    cy.get('#password').clear()
    cy.get('#login-button').click()
    cy.contains('Epic sadface: Password is required').should('be.visible')
    })
    
    it('should display error message for special characters in username', () => {
    cy.get('#user-name').type('#$%^&*')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.contains('Epic sadface: Username and password do not match any user in this service').should('be.visible')
    })
    
    it('should display error message for special characters in password', () => {
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('#$%^&*')
    cy.get('#login-button').click()
    cy.contains('Epic sadface: Username and password do not match any user in this service').should('be.visible')
    })
    
    it('should display error message for uppercase username', () => {
    cy.get('#user-name').type('STANDARD_USER')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.contains('Epic sadface: Username and password do not match any user in this service').should('be.visible')
    })
    
    it('should display error message for uppercase password', () => {
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('SECRET_SAUCE')
    cy.get('#login-button').click()
    cy.contains('Epic sadface: Username and password do not match any user in this service').should('be.visible')
})
})
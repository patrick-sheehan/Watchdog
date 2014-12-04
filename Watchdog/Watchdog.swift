//
//  Watchdog.swift
//  Watchdog
//
//  Created by Patrick Sheehan on 12/4/14.
//  Copyright (c) 2014 Appuccino. All rights reserved.
//

import Foundation

class Watchdog {
    
    var minLength = 10
    var maxLength = 140
    
    // optional value, allow any character if not set
    var validCharacters: String?
    
    var isBlockingPhoneNumbers = true
    var isBlockingEmailAddresses = true
    
    
    func shouldSubmit(message: String) {

    }
    
    func isValidLength(message: String) {
        
    }
    
    func hasValidCharacters(message: String) {
        
    }
    
    func shouldBlockForNumber(message: String) {
        
    }
    
    func shouldBlockForEmail(message: String) {
        
    }
    
    func shouldBlockForVulgar(message: String) {
        
    }
    
    func shouldBlockForSexual(message: String) {
        
    }
    
    
}
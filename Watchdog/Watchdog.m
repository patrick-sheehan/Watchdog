//
//  Watchdog.m
//  Watchdog
//
//  Created by Patrick Sheehan on 12/2/14.
//  Copyright (c) 2014 Appuccino. All rights reserved.
//

#import "Watchdog.h"

@interface Watchdog()

@property (nonatomic) int minLength;
@property (nonatomic) int maxLength;
@property (nonatomic) BOOL blockPhoneNumbers;
@property (nonatomic) BOOL blockEmailAddresses;

@end

@implementation Watchdog

- (id)initWithOptions:(NSDictionary *)options
{
    self = [super init];
    if (self)
    {
        NSNumber *minLength = [options objectForKey:@"minLength"];
        NSNumber *maxLength = [options objectForKey:@"maxLength"];
        NSNumber *blockPhoneNumbers = [options objectForKey:@"blockPhoneNumbers"];
        NSNumber *blockEmailAddresses = [options objectForKey:@"blockEmailAddresses"];
        
        self.minLength = (minLength == nil) ? 10 : [minLength intValue];
        self.maxLength = (maxLength == nil) ? 140 : [maxLength intValue];
        self.blockPhoneNumbers = (blockPhoneNumbers == nil) ? NO : [blockPhoneNumbers boolValue];
        self.blockEmailAddresses = (blockEmailAddresses == nil) ? NO : [blockEmailAddresses boolValue];
    }
    
    return self;
}
- (BOOL)shouldSubmitMessage:(NSString*)message
                WithResults:(NSMutableDictionary *)results
{
    BOOL isValidLength = [self isValidLength:message];
    [results setValue:[NSNumber numberWithBool:isValidLength]
               forKey:@"isValidLength"];
    
    BOOL hasValidCharacters = [self hasValidCharacters:message];
    [results setValue:[NSNumber numberWithBool:hasValidCharacters]
               forKey:@"hasValidCharacters"];
    
    BOOL shouldBlockForNumber = [self shouldBlockForNumber:message];
    [results setValue:[NSNumber numberWithBool:shouldBlockForNumber]
               forKey:@"shouldBlockForNumber"];
    
    BOOL shouldBlockForEmail = [self shouldBlockForEmail:message];
    [results setValue:[NSNumber numberWithBool:shouldBlockForEmail]
               forKey:@"shouldBlockForEmail"];
    
    BOOL shouldBlockForVulgar = [self shouldBlockForVulgar:message];
    [results setValue:[NSNumber numberWithBool:shouldBlockForVulgar]
               forKey:@"shouldBlockForVulgar"];
    
    BOOL shouldBlockForSexual = [self shouldBlockForSexual:message];
    [results setValue:[NSNumber numberWithBool:shouldBlockForSexual]
               forKey:@"shouldBlockForSexual"];
    
    return isValidLength && hasValidCharacters
    && !shouldBlockForNumber && !shouldBlockForEmail
    && !shouldBlockForSexual && !shouldBlockForVulgar;
}

- (BOOL)isValidLength:(NSString*) message
{
    NSUInteger length = message.length;
    
    if (length < self.minLength || length > self.maxLength)
    {
        NSLog(@"LENGTH REJECTION: %@", message);
        return NO;
    }
    
    return YES;
}
- (BOOL)hasValidCharacters:(NSString*) message
{
    
    return YES;
}
- (BOOL)shouldBlockForNumber:(NSString*) message
{
    NSUInteger len = [message length];
    unichar buffer[len+1];
    
    [message getCharacters:buffer range:NSMakeRange(0, len)];
    
    //    NSLog(@"getCharacters:range: with unichar buffer");
    int numCount = 0;
    for(int i = 0; i < len; i++) {
        if (isdigit(buffer[i]))
            numCount++;
        NSLog(@"%C", buffer[i]);
    }
    
    if (numCount == 10)
    {
        NSLog(@"PHONE NUMBER REJECTION: %@", message);
        return YES;
        
    }
    
    return NO;
}
- (BOOL)shouldBlockForEmail:(NSString*) message
{
    NSString *emailRegex = @"[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,6}";
    NSPredicate *emailTest = [NSPredicate predicateWithFormat:@"SELF MATCHES %@", emailRegex];
    if ([emailTest evaluateWithObject:message])
    {
        NSLog(@"EMAIL REJECTION: %@", message);
        return YES;
    }
    
    return NO;
}
- (BOOL)shouldBlockForVulgar:(NSString*) message
{
    NSString* path = [[NSBundle mainBundle] pathForResource:@"bad_words"
                                                     ofType:@"txt"];
    NSArray *badWords = [[NSString stringWithContentsOfFile:path
                                                   encoding:NSUTF8StringEncoding
                                                      error:NULL]
                         componentsSeparatedByString:@"\n"];
    
    for (NSString *word in [message componentsSeparatedByString:@" "])
    {
        if ([badWords containsObject:word])
        {
            return YES;
        }
    }
    
    return NO;
}
- (BOOL)shouldBlockForSexual:(NSString*) message
{
    
    return NO;
}
@end

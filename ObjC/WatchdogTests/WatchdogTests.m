//
//  WatchdogTests.m
//  Watchdog
//
//  Created by Patrick Sheehan on 12/4/14.
//  Copyright (c) 2014 Appuccino. All rights reserved.
//

//#import <Cocoa/Cocoa.h>
#import <XCTest/XCTest.h>

#import "Watchdog.h"

@interface WatchdogTests : XCTestCase

@property (strong) Watchdog* myWatchDog;

@end

@implementation WatchdogTests

- (void)setUp {
    [super setUp];
    // Put setup code here. This method is called before the invocation of each test method in the class.
    
    NSDictionary *options = [[NSDictionary alloc] initWithObjectsAndKeys:
                             [NSNumber numberWithInt:10], @"minLength",
                             [NSNumber numberWithInt:140], @"maxLength",
                             [NSNumber numberWithBool:YES], @"blockPhoneNumbers",
                             [NSNumber numberWithBool:YES], @"blockEmailAddresses",
                             nil];
    
    
//    _myWatchDog = [[Watchdog alloc] initWithOptions:options];
    
}

- (void)tearDown {
    // Put teardown code here. This method is called after the invocation of each test method in the class.
    [super tearDown];
}

- (void)testExample {
    // This is an example of a functional test case.
    
    XCTAssert(YES, @"Pass");
}

- (void)testPerformanceExample {
    // This is an example of a performance test case.
    [self measureBlock:^{
        // Put the code you want to measure the time of here.
    }];
}

@end

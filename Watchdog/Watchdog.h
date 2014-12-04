//
//  Watchdog.h
//  Watchdog
//
//  Created by Patrick Sheehan on 12/2/14.
//  Copyright (c) 2014 Appuccino. All rights reserved.
//

#import <Foundation/Foundation.h>
//#import <Python.h>

@interface Watchdog : NSObject

@property (strong, nonatomic) NSObject* myContentWatchdog;
@property (strong, nonatomic) id stuff;

- (NSArray *) arrayOfNamedStrings;
//- (void) pyTestMethod;

@end

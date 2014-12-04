//
//  Watchdog.m
//  Watchdog
//
//  Created by Patrick Sheehan on 12/2/14.
//  Copyright (c) 2014 Appuccino. All rights reserved.
//

#import "Watchdog.h"

@class PythonStuff;

@interface NSObject (MyNewMethods)
//- (void) pyTestMethod;
@end

@implementation Watchdog

- (id)init
{
    self = [super init];
    Class ContentWatchDogClass = NSClassFromString(@"ContentWatchdog");
    self.myContentWatchdog = [ContentWatchDogClass new];
    
    
    return self;
}

- (NSArray *) arrayOfNamedStrings;
{
    if (!_stuff) {
        Class PythonStuffClass = NSClassFromString(@"PythonStuff");
        _stuff = [PythonStuffClass new];
    }
    return [_stuff arrayOfNamedStrings];
}
@end

using NUnit.Allure.Core;
using NUnit.Framework;
using Allure.NUnit.Attributes;
using System;

[TestFixture]
[AllureNUnitAttribute]
public class Tests
{
    [Test]
    
    public void IgnoredTest()
    {
        Assert.Pass();
    }
    
    [Test2]
    public void WorkingTest()
    {
        Assert.Pass();
    }
}

internal class Test2Attribute : Attribute
{
}
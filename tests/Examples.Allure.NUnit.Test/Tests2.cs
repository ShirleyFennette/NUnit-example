using NUnit.Allure.Core;
using NUnit.Framework;
using Allure.NUnit.Attributes;
using System;

[TestFixture]
#pragma warning disable CS0618 // Type or member is obsolete
[AllureNUnit]
#pragma warning restore CS0618 // Type or member is obsolete
public class Tests2
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

internal class Test23Attribute : Attribute
{
}